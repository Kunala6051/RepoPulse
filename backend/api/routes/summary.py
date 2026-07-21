from fastapi import APIRouter

router = APIRouter(prefix="/summary", tags=["summary"])


@router.get("")
async def get_summary() -> dict:
    """TODO: return latest Summary agent output."""
    return {}
