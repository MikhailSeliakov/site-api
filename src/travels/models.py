from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean


metadata = MetaData()


travels = Table(
    "travels",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("created_by", Integer, nullable=False),
    Column("location_start", String(length=64)),
    Column("location_end", String(length=64)),
    Column("date_start", String(length=64), nullable=False),
    Column("date_end", String(length=64)),
    Column("header", String(length=128)),
    Column("description", String(length=2000)),
    Column("travel_type", String(length=50)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_promo", Boolean, default=False, nullable=False),
    Column("promo_type", Integer),
    Column("is_hidden", Boolean, default=False, nullable=False),
    Column("is_deleted", Boolean, default=False, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("preferred_gender", Integer, default=2),
)
