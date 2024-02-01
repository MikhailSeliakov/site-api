from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean


metadata = MetaData()


sports = Table(
    "sports",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("created_by", Integer, nullable=False),
    Column("location", String(length=64)),
    Column("date", String(length=64), nullable=False),
    Column("header", String(length=128)),
    Column("description", String(length=2000)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_promo", Boolean, default=False, nullable=False),
    Column("promo_type", Integer),
    Column("is_hidden", Boolean, default=False, nullable=False),
    Column("is_deleted", Boolean, default=False, nullable=False),
    Column("is_online", Boolean, default=False, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("preferred_gender", Integer, default=2),
)
