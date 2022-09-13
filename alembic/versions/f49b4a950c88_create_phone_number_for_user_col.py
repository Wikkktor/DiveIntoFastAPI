"""Create phone number for user col

Revision ID: f49b4a950c88
Revises: 
Create Date: 2022-09-13 11:29:03.591471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f49b4a950c88'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column("phone_number", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_table('users', "phone_number")
