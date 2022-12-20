"""create post table

Revision ID: 1b687b55f183
Revises: 1ccf84938fb2
Create Date: 2022-09-12 14:58:38.169143

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "1b687b55f183"
down_revision = "1ccf84938fb2"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column("contents", sa.String(length=255), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.ARRAY("comments", UUID(as_uuid=True)),
        sa.ARRAY("tags", UUID(as_uuid=True)),
        sa.Column("users_id", UUID(as_uuid=True), sa.ForeignKey("users.id")),
        sa.Column("like", sa.Integer()),
    )


def downgrade():
    op.drop_constraint("users_id", "users")
    op.drop_table("posts")
