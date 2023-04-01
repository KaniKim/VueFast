"""add column to comment table

Revision ID: d9f326d537c2
Revises: 81695d26a012
Create Date: 2023-04-01 17:06:20.387832

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "d9f326d537c2"
down_revision = "81695d26a012"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "comments",
        sa.Column("posts_id", UUID(as_uuid=True), sa.ForeignKey("posts.id")),
    )


def downgrade():
    op.drop_column("comments", "posts")
