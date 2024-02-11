"""empty message

Revision ID: bbaa436e24f5
Revises: 1e4b6110f48a
Create Date: 2024-02-11 16:48:02.031751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbaa436e24f5'
down_revision: Union[str, None] = '1e4b6110f48a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetings_events',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
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
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id', 'created_by'),
    sa.UniqueConstraint('id')
    )
    op.create_table('meetings_events_interests',
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('interest', sa.String(), nullable=False),
    sa.Column('added_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['meetings_events.id'], ),
    sa.ForeignKeyConstraint(['interest'], ['meetings_interests.interest'], ),
    sa.PrimaryKeyConstraint('event_id', 'interest')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meetings_events_interests')
    op.drop_table('meetings_events')
    # ### end Alembic commands ###
