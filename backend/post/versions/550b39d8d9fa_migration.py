"""migration

Revision ID: 550b39d8d9fa
Revises: 
Create Date: 2022-03-01 15:18:39.447995

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = "550b39d8d9fa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "post",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("title", sa.String(50)),
        sa.Column("description", sa.Text(100), nullable=True),
        sa.Column("content", sa.Text()),
        sa.Column("created_at", sa.DateTime, default=datetime.datetime.now),
        sa.Column("modified_at", sa.DateTime, default=datetime.datetime.now),
    )


def downgrade():
    op.drop_table("post")
