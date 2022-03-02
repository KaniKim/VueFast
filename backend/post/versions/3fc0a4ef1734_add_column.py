"""add column

Revision ID: 3fc0a4ef1734
Revises: f08c6ee8c811
Create Date: 2022-03-02 09:40:29.886612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3fc0a4ef1734"
down_revision = "f08c6ee8c811"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("user", sa.Column("hashed_password", sa.String()))


def downgrade():
    op.drop_column("user", "hashed_password")
