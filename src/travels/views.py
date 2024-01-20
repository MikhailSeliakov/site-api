from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(prefix="/api/v1/travel", tags=["Travels"])


@router.get("")
def get_travels():
    return {
        "travelsId": [
            "Item1",
            "Item2",
            "Item3",
        ]
    }


@router.get("/{travel_id}")
def get_info_travel_by_id(travel_id: Annotated[int, Path(..., ge=1)]):
    return {
        "travelId": travel_id
    }
