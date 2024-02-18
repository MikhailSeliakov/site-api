from datetime import date
from enum import Enum
from typing import Optional, Literal
from pydantic import BaseModel, Field


class InterestMeetingSchema(BaseModel):
    id: int
    interest: str
    interest_ru: str
    is_active: bool


class GenderOptions(Enum):
    male = "male"
    female = "female"
    none = None


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
    preferredGender: GenderOptions


class AvailableMeetingsSchema(BaseModel):
    id: int
    createdBy: int
    location: str
    date: date
    header: str
    description: str
    preferredGender: int
    interest: list
