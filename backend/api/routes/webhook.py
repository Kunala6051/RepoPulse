from fastapi import APIRouter, HTTPException, Request

from backend.config.settings import settings
from backend.services.github_service import GitHubService

router = APIRouter(prefix="/webhook", tags=["webhook"])
github_service = GitHubService()


@router.post("/github")
async def github_webhook(request: Request) -> dict[str, str]:
    """TODO: validate signature, publish WebhookEvent to Redis."""
    if not settings.github_webhook_secret:
        raise HTTPException(
            status_code=503,
            detail="GitHub webhook secret is not configured",
        )

    payload = await request.body()
    signature = request.headers.get("x-hub-signature-256", "")
    if not await github_service.verify_signature(payload, signature):
        raise HTTPException(status_code=401, detail="Invalid GitHub webhook signature")

    return {"status": "received"}
