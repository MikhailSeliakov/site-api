from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class InterestMeetingSchema(BaseModel):
    id: int
    interest: str
    interest_ru: str
    is_active: bool


class CreateMeetingSchema(BaseModel):
    """
    Свойства указаны в camelCase т.к. фронт запросил такой формат.
    """
    interests: list
    isOnline: bool
    location: Optional[str]
    dateStart: date
    hourStart: int = Field(..., ge=0, le=23)
    minuteStart: int = Field(..., ge=0, le=59)
    header: str = Field(..., max_length=100)
    aboutMeeting: str = Field(..., max_length=500)
    requiredAge: str
    preferredGender: int = Field(..., ge=0, le=2)
