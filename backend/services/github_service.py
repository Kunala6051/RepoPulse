import hashlib
import hmac

from backend.config.settings import settings


class GitHubService:
    """TODO: fetch commit/file diffs via GitHub API."""

    async def verify_signature(self, payload: bytes, signature: str) -> bool:
        """Verify GitHub's SHA-256 signature against the raw request body."""
        secret = settings.github_webhook_secret
        if not secret or not signature.startswith("sha256="):
            return False

        try:
            provided_signature = signature.encode("ascii")
        except UnicodeEncodeError:
            return False

        digest = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()
        expected_signature = f"sha256={digest}".encode("ascii")
        return hmac.compare_digest(provided_signature, expected_signature)

    async def get_commit_diff(self, owner: str, repo: str, sha: str) -> str:
        """TODO"""
