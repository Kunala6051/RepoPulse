from fastapi import APIRouter

router = APIRouter(prefix="/webhook", tags=["webhook"])


@router.post("/github")
async def github_webhook() -> dict:
    """TODO: validate signature, publish WebhookEvent to Redis."""
    return {"status": "received"}
