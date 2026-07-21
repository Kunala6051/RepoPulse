from fastapi import APIRouter

router = APIRouter(prefix="/technical-debt", tags=["technical-debt"])


@router.get("")
async def get_technical_debt() -> dict:
    """TODO: return latest TechDebtReport."""
    return {}
