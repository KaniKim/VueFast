"""post

Revision ID: f08c6ee8c811
Revises: 
Create Date: 2022-03-02 09:05:45.568098

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = "f08c6ee8c811"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "post",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("title", sa.String(50)),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("content", sa.Text()),
        sa.Column("created_at", sa.DateTime, default=datetime.datetime.now),
        sa.Column("modified_at", sa.DateTime, default=datetime.datetime.now),
    )
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.ARRAY(sa.String(100), as_tuple=False, dimensions=None, zero_indexes=False),
        sa.Column("post_id", sa.Integer(), sa.ForeignKey("post.id")),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.Column("email", sa.String(), index=True, nullable=False),
        sa.Column("name", sa.String()),
        sa.Column("disabled", sa.Boolean(), default=False),
        sa.Column("post_id", sa.Integer(), sa.ForeignKey("post.id")),
    )


def downgrade():
    op.drop_table("post")
    op.drop_table("tags")
    op.drop_table("user")
