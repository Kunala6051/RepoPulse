from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("")
async def post_chat_message() -> dict:
    """TODO: forward question to the Q&A agent and return a grounded answer."""
    return {}
