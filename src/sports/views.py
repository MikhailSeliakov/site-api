from typing import Annotated
from fastapi import APIRouter, Path
from src.sports import crud

router = APIRouter(prefix="/api/v1/sport", tags=["Sports"])


@router.get("")
def get_sports():
    return {
        "sportId": [
            "Item1",
            "Item2",
            "Item3",
        ]
    }


@router.get("/{sport_id}")
def get_info_sport_by_id(sport_id: Annotated[int, Path(..., ge=1)]):
    return {
        "sportId": sport_id
    }


@router.post("/create")
def create_sport_event():
    return crud.create_sport_event()
