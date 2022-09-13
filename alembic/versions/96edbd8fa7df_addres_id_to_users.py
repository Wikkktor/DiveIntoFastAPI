"""Addres id to users

Revision ID: 96edbd8fa7df
Revises: 923991c5b9b4
Create Date: 2022-09-13 11:50:45.403721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96edbd8fa7df'
down_revision = '923991c5b9b4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address",
                          local_cols=["address_id"], remote_cols=["id"], ondelete="CASCADE")



def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name='users')
    op.drop_column("users", 'address_id')
