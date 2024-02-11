"""empty message

Revision ID: 1e4b6110f48a
Revises: 364beec6fb07
Create Date: 2024-02-11 16:42:37.424039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1e4b6110f48a'
down_revision: Union[str, None] = '364beec6fb07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meetings_events_interests')
    op.drop_table('meetings_events')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetings_events',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('meetings_events_id_seq'::regclass)"), autoincrement=True, nullable=False),
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
    sa.PrimaryKeyConstraint('id', 'created_by', name='meetings_events_pkey'),
    sa.UniqueConstraint('id', name='meetings_events_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('meetings_events_interests',
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('interest', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('added_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['meetings_events.id'], name='meetings_events_interests_event_id_fkey'),
    sa.ForeignKeyConstraint(['interest'], ['meetings_interests.interest'], name='meetings_events_interests_interest_fkey'),
    sa.PrimaryKeyConstraint('event_id', 'interest', name='meetings_events_interests_pkey')
    )
    # ### end Alembic commands ###