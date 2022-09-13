"""Create another table

Revision ID: 923991c5b9b4
Revises: f49b4a950c88
Create Date: 2022-09-13 11:39:44.100619

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '923991c5b9b4'
down_revision = 'f49b4a950c88'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("address", sa.String(), nullable=False),
                    sa.Column("address2", sa.String(), nullable=False),
                    sa.Column("city", sa.String(), nullable=False),
                    sa.Column("post_code", sa.String(), nullable=False),
                    sa.Column("country", sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('address')
