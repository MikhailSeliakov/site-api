from typing import Annotated
from fastapi import APIRouter, Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.meetings.schemas import CreateMeetingSchema
from src.meetings.service import MeetingService
from src.users.schemas import UserSchema
from src.users.views import get_current_auth_user

router = APIRouter(prefix="/api/v1/meetings", tags=["Meetings"])


@router.get("")
def get_available_meetings():
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
def create_meeting(
        meeting_info: CreateMeetingSchema,
        user: UserSchema = Depends(get_current_auth_user),
        session: AsyncSession = Depends(get_async_session),
):
    return MeetingService(session).create_meeting(user.id, meeting_info)


@router.delete("/{meeting_id}")
def delete_meeting_event():
    return {}
