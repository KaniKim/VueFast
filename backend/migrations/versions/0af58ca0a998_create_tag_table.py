"""create tag table

Revision ID: 0af58ca0a998
Revises: b5fab611b16c
Create Date: 2022-09-12 14:59:02.894936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "0af58ca0a998"
down_revision = "b5fab611b16c"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tags",
        sa.Column("id", UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column("contents", sa.String(length=255), nullable=False),
        sa.Column("users_id", UUID(as_uuid=True), sa.ForeignKey("users.id")),
        sa.Column("posts_id", UUID(as_uuid=True), sa.ForeignKey("posts.id")),
    )


def downgrade():
    op.drop_constraint("users_id", "users")
    op.drop_constraint("posts_id", "posts")
    op.drop_table("tags")
