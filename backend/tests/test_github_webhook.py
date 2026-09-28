import asyncio
import hashlib
import hmac

import pytest
from fastapi import HTTPException
from starlette.requests import Request
from starlette.types import Message, Scope

from backend.api.routes import webhook
from backend.config.settings import settings
from backend.services.github_service import GitHubService


def _signature(payload: bytes, secret: str) -> str:
    digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def _request(payload: bytes, signature: str) -> Request:
    headers = [(b"x-hub-signature-256", signature.encode("ascii"))]
    scope: Scope = {
        "type": "http",
        "method": "POST",
        "path": "/webhook/github",
        "headers": headers,
    }

    async def receive() -> Message:
        return {"type": "http.request", "body": payload, "more_body": False}

    return Request(scope, receive)


@pytest.mark.parametrize(
    "signature_valid",
    [True, False],
)
def test_verify_signature(
    monkeypatch: pytest.MonkeyPatch,
    signature_valid: bool,
) -> None:
    payload = b'{"ref":"refs/heads/main"}'
    secret = "test-secret"
    monkeypatch.setattr(settings, "github_webhook_secret", secret)
    signature = _signature(payload, secret) if signature_valid else "sha256=invalid"

    assert (
        asyncio.run(GitHubService().verify_signature(payload, signature))
        is signature_valid
    )


def test_verify_signature_rejects_missing_secret(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(settings, "github_webhook_secret", "")

    signature = _signature(b"payload", "secret")
    assert not asyncio.run(GitHubService().verify_signature(b"payload", signature))


def test_github_webhook_accepts_signed_payload(monkeypatch: pytest.MonkeyPatch) -> None:
    payload = b'{"ref":"refs/heads/main"}'
    secret = "test-secret"
    monkeypatch.setattr(settings, "github_webhook_secret", secret)

    response = asyncio.run(
        webhook.github_webhook(_request(payload, _signature(payload, secret)))
    )

    assert response == {"status": "received"}


def test_github_webhook_rejects_invalid_signature(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(settings, "github_webhook_secret", "test-secret")

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(webhook.github_webhook(_request(b"payload", "sha256=invalid")))

    assert exc_info.value.status_code == 401


def test_github_webhook_fails_when_secret_is_unconfigured(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(settings, "github_webhook_secret", "")

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(webhook.github_webhook(_request(b"payload", "")))

    assert exc_info.value.status_code == 503
