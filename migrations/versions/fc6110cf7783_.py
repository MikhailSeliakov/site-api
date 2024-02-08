"""empty message

Revision ID: fc6110cf7783
Revises: b5d3c0deb9c6
Create Date: 2024-02-08 12:06:11.554961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fc6110cf7783'
down_revision: Union[str, None] = 'b5d3c0deb9c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('travels_events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('location_start', sa.String(length=64), nullable=True),
    sa.Column('location_end', sa.String(length=64), nullable=True),
    sa.Column('date_start', sa.String(length=64), nullable=False),
    sa.Column('date_end', sa.String(length=64), nullable=True),
    sa.Column('header', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=2000), nullable=True),
    sa.Column('travel_type', sa.String(length=50), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_promo', sa.Boolean(), nullable=False),
    sa.Column('promo_type', sa.Integer(), nullable=True),
    sa.Column('is_hidden', sa.Boolean(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('preferred_gender', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sports_events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('date', sa.String(length=64), nullable=False),
    sa.Column('header', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=2000), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_promo', sa.Boolean(), nullable=False),
    sa.Column('promo_type', sa.Integer(), nullable=True),
    sa.Column('is_hidden', sa.Boolean(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('is_online', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('preferred_gender', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meetings_events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('date', sa.String(length=64), nullable=False),
    sa.Column('header', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=2000), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_promo', sa.Boolean(), nullable=False),
    sa.Column('promo_type', sa.Integer(), nullable=True),
    sa.Column('is_hidden', sa.Boolean(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('is_online', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('preferred_gender', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sports')
    op.drop_table('travels')
    op.drop_table('meetings')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetings',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_by', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('location', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('date', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('header', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=2000), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_promo', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('promo_type', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_hidden', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_online', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('preferred_gender', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='meetings_pkey')
    )
    op.create_table('travels',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_by', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('location_start', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('location_end', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('date_start', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('date_end', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('header', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=2000), autoincrement=False, nullable=True),
    sa.Column('travel_type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_promo', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('promo_type', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_hidden', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('preferred_gender', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='travels_pkey')
    )
    op.create_table('sports',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_by', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('location', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('date', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('header', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=2000), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_promo', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('promo_type', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_hidden', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_online', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('preferred_gender', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='sports_pkey')
    )
    op.drop_table('meetings_events')
    op.drop_table('sports_events')
    op.drop_table('travels_events')
    # ### end Alembic commands ###
