"""create category table

Revision ID: 5387693e06f4
Revises: 1b687b55f183
Create Date: 2022-09-12 14:58:53.477389

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "5387693e06f4"
down_revision = "1b687b55f183"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "category",
        sa.Column("id", UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.ARRAY("posts_id", UUID(as_uuid=True)),
    )


def downgrade():
    pass
