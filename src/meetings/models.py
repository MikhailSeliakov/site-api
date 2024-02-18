from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, ForeignKey
from src.users.models import users

metadata = MetaData()


meetings_events = Table(
    "meetings_events",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("created_by", Integer, ForeignKey(users.c.id), primary_key=True, nullable=False),
    Column("location", String(length=64)),
    Column("date", String(length=64), nullable=False),
    Column("header", String(length=128)),
    Column("description", String(length=2000)),
    Column("hour_start", Integer, nullable=False),
    Column("minutes_start", Integer, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_promo", Boolean, default=False, nullable=False),
    Column("promo_type", Integer),
    Column("is_hidden", Boolean, default=False, nullable=False),
    Column("is_deleted", Boolean, default=False, nullable=False),
    Column("is_online", Boolean, default=False, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("preferred_gender", String),
)

meetings_interests = Table(
    "meetings_interests",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("interest", String, unique=True),
    Column("interest_ru", String, unique=True),
    Column("is_active", Boolean, nullable=False),
)

meetings_events_interests = Table(
    "meetings_events_interests",
    metadata,
    Column("event_id", Integer, ForeignKey(meetings_events.c.id), primary_key=True),
    Column("interest", String, ForeignKey(meetings_interests.c.interest), primary_key=True),
    Column("added_at", TIMESTAMP, default=datetime.utcnow),
)
