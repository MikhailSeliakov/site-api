from sqlalchemy.ext.asyncio import AsyncSession
from src.meetings.schemas import CreateMeetingSchema


class MeetingService:

    def __init__(self, session):
        self.session: AsyncSession = session

    def create_meeting(self, user_id: int, meeting_info: CreateMeetingSchema):
        return {
            "success": True
        }
