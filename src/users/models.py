from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, ForeignKey
from src.sports.models import sports_interests
from src.meetings.models import meetings_interests

metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("phone_number", String(length=11)),
    Column("first_name", String(length=64)),
    Column("last_name", String(length=64)),
    Column("patronymic_name", String(length=64)),
    Column("location", String(length=64)),
    Column("birth_date", String(length=64)),
    Column("about", String(length=1024)),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

users_interests = Table(
    "users_interests",
    metadata,
    Column("user_id", Integer, ForeignKey(users.c.id), primary_key=True),
    Column("sport_interest_id", Integer, ForeignKey(sports_interests.c.id), primary_key=True),
    Column("meeting_interest_id", Integer, ForeignKey(meetings_interests.c.id), primary_key=True)
)
