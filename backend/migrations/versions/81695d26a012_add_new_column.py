"""add new column

Revision ID: 81695d26a012
Revises: 0af58ca0a998
Create Date: 2022-12-26 06:11:59.572576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "81695d26a012"
down_revision = "0af58ca0a998"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users",
        sa.Column("refresh_token", sa.String(length=255), nullable=True),
    )


def downgrade():
    op.drop_column("users", "refresh_token")
