"""create comment table

Revision ID: b5fab611b16c
Revises: 5387693e06f4
Create Date: 2022-09-12 14:58:58.412134

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'b5fab611b16c'
down_revision = '5387693e06f4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "comments",
        sa.Column("id", UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column("contents", sa.String(length=255), nullable=False),
        sa.Column("users_id", UUID(as_uuid=True), sa.ForeignKey("users.id")),
        sa.Column("like", sa.Integer())
    )


def downgrade():
    op.drop_constraint("users_id", "users")
    op.drop_table("comments")
