from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class InterestMeetingSchema(BaseModel):
    id: int
    interest: str
    interest_ru: str
    is_active: bool


class CreateMeetingSchema(BaseModel):
    interests: list
    is_online: bool
    location: Optional[str]
    date_start: date
    hour_start: int = Field(..., ge=0, le=23)
    minute_start: int = Field(..., ge=0, le=59)
    header: str = Field(..., max_length=100)
    about_meeting: str = Field(..., max_length=500)
    required_age: str
    preferred_gender: int = Field(..., ge=0, le=2)
