from fastapi import APIRouter

from app.models import Farm

router = APIRouter()


@router.get("", response_model=list[Farm])
def read_farms() -> list[Farm]:
    farms = [
        Farm(id=1, crop="wheat"),
        Farm(id=2, crop="barley"),
        Farm(id=3, crop="hops"),
    ]

    return farms
