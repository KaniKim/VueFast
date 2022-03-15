"""add column, association

Revision ID: b965c3a518c9
Revises: 3fc0a4ef1734
Create Date: 2022-03-06 14:01:41.138553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b965c3a518c9"
down_revision = "3fc0a4ef1734"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "association_table",
        sa.Column("post_id", sa.Integer, sa.ForeignKey("post.id")),
        sa.Column("tags_id", sa.Integer, sa.ForeignKey("tags.id")),
    )


def downgrade():
    op.drop_table("association_table")
