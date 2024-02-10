from pydantic import BaseModel


class InterestMeetingSchema(BaseModel):
    id: int
    interest: str
    interest_ru: str
    is_active: bool
