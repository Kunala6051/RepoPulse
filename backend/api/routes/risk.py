from fastapi import APIRouter

router = APIRouter(prefix="/risk", tags=["risk"])


@router.get("")
async def get_risk() -> dict:
    """TODO: return latest RiskReport."""
    return {}
