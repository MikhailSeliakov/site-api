from typing import Annotated
from fastapi import APIRouter, Path
from src.meetings import crud

router = APIRouter(prefix="/api/v1/meetings", tags=["Meetings"])


@router.get("")
def get_meetings():
    return {
        "meetingId": [
            "Item1",
            "Item2",
            "Item3",
        ]
    }


@router.get("/{meeting_id}")
def get_info_meeting_by_id(meeting_id: Annotated[int, Path(..., ge=1)]):
    return {
        "meetingId": meeting_id
    }


@router.post("")
def create_meeting():
    return crud.create_meeting()


@router.delete("/{meeting_id}")
def delete_meeting_event():
    return crud.create_meeting()
