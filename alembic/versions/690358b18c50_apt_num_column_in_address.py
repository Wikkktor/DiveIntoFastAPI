"""apt num column in address

Revision ID: 690358b18c50
Revises: 96edbd8fa7df
Create Date: 2022-09-13 12:32:41.629821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '690358b18c50'
down_revision = '96edbd8fa7df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
