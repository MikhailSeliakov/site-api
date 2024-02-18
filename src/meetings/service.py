import uuid
from collections import defaultdict
from datetime import datetime
from fastapi.responses import JSONResponse
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.meetings.models import meetings_events, meetings_events_interests
from src.meetings.schemas import CreateMeetingSchema
from src.users.service import UserService


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def move_interest_to_end(dictionary):
    interest = dictionary.pop('interest')
    dictionary['interest'] = interest


class MeetingService:

    def __init__(self, session):
        self.session: AsyncSession = session

    async def create_meeting(self, user_id: int, meeting_info: CreateMeetingSchema):
        available_meetings, available_sports = await UserService(self.session).get_available_interests()
        available_meetings_keys = [item.get("name") for item in available_meetings]

        if not all(item in available_meetings_keys for item in meeting_info.interests):
            return JSONResponse(status_code=200, content={
                "success": False,
                "data": {
                    "message": "Попытка установить несуществующий интерес по встречам",
                    "uuid": uuid.uuid4().hex,
                    "payload": meeting_info.interests,
                    "availableInterests": available_meetings,
                }
            })

        stmt = insert(meetings_events).values(
            created_by=user_id,
            location=meeting_info.location,
            date=meeting_info.dateStart.__str__(),
            header=meeting_info.header,
            hour_start=meeting_info.hourStart,
            minutes_start=meeting_info.minuteStart,
            description=meeting_info.aboutMeeting,
            is_online=meeting_info.isOnline,
            created_at=datetime.utcnow(),
            preferred_gender=meeting_info.preferredGender.value,
        ).returning(meetings_events.c.id)
        created_event_id = await self.session.execute(stmt)
        created_event_id = created_event_id.first()[0]
        stmt_2 = insert(meetings_events_interests).values(
            [{"event_id": created_event_id, "interest": item} for item in list(set(meeting_info.interests))]
        )
        await self.session.execute(stmt_2)
        await self.session.commit()
        return {
            "success": True,
            "data": {
                "message": "Встреча создана",
                "eventId": created_event_id
            }
        }

    async def get_available_meetings(self):
        try:
            get_active_events = (
                select(
                    meetings_events.c.id,
                    meetings_events.c.created_by,
                    meetings_events.c.location,
                    meetings_events.c.date,
                    meetings_events.c.header,
                    meetings_events.c.hour_start,
                    meetings_events.c.minutes_start,
                    meetings_events.c.description,
                    meetings_events.c.preferred_gender,
                    meetings_events_interests.c.interest
                ).join(meetings_events_interests, meetings_events.c.id == meetings_events_interests.c.event_id)
                .where(meetings_events.c.is_active)
                .where(meetings_events.c.is_deleted == False)
                .where(meetings_events.c.is_hidden == False)
            )
            result_query = await self.session.execute(get_active_events)
            available_meetings = result_query.mappings().all()
            final_result = [{to_camel_case(key): value for key, value in item.items()} for item in available_meetings]
            grouped_data = defaultdict(lambda: {'interest': []})

            for item in final_result:
                id_ = item['id']
                grouped_data[id_].update({key: value for key, value in item.items() if key != 'interest'})
                grouped_data[id_]['interest'].append(item['interest'])

            final_data = list(grouped_data.values())

            for item in final_data:
                move_interest_to_end(item)

            return JSONResponse(status_code=200, content={
                "success": True,
                "data": {
                    "meetings": final_data
                }
            })
        except Exception:
            return JSONResponse(status_code=200, content={
                "success": False,
                "data": {
                    "message": "Произошла внутренняя ошибка сервера. При повторении ошибки обратитесь в поддержку.",
                    "uuid": uuid.uuid4().hex,
                }
            })
