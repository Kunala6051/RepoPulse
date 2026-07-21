from fastapi import APIRouter

router = APIRouter(prefix="/repositories", tags=["repositories"])


@router.get("")
async def list_repositories() -> list[dict]:
    """TODO: return connected repositories."""
    return []
