from fastapi import APIRouter

router = APIRouter(prefix="/activity", tags=["activity"])


@router.get("")
async def get_activity() -> list[dict]:
    """TODO: return recent pipeline activity events."""
    return []
