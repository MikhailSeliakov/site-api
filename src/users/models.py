from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, ForeignKey

metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("phone_number", String(length=11), primary_key=True, unique=True),
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


from src.meetings.models import meetings_interests
users_meetings_interests = Table(
    "users_meetings_interests",
    metadata,
    Column("user_id", Integer, ForeignKey(users.c.id), primary_key=True),
    Column("interest", String, ForeignKey(meetings_interests.c.interest), primary_key=True),
    Column("added_at", TIMESTAMP, default=datetime.utcnow)
)


from src.sports.models import sports_interests
users_sports_interests = Table(
    "users_sports_interests",
    metadata,
    Column("user_id", Integer, ForeignKey(users.c.id), primary_key=True),
    Column("interest", String, ForeignKey(sports_interests.c.interest), primary_key=True),
    Column("added_at", TIMESTAMP, default=datetime.utcnow)
)
