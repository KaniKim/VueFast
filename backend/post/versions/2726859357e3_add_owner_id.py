"""add owner_id

Revision ID: 2726859357e3
Revises: b965c3a518c9
Create Date: 2022-03-06 14:36:38.668074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2726859357e3"
down_revision = "b965c3a518c9"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("post", sa.Column("owner_id", sa.String()))


def downgrade():
    pass
