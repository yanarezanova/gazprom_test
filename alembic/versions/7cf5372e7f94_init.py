"""create initial tables

Revision ID: 0001_initial
Revises:
Create Date: 2025-04-13 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, nullable=False, unique=True, index=True),
    )

    op.create_table(
        'devices',
        sa.Column('id', sa.String, primary_key=True, index=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=True),
    )

    op.create_table(
        'device_statistics',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('device_id', sa.String, nullable=False, index=True),
        sa.Column('timestamp', sa.DateTime, nullable=False, server_default=sa.func.now(), index=True),
        sa.Column('x', sa.Float, nullable=False),
        sa.Column('y', sa.Float, nullable=False),
        sa.Column('z', sa.Float, nullable=False),
    )


def downgrade():
    op.drop_table('device_statistics')
    op.drop_table('devices')
    op.drop_table('users')
