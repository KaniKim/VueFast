"""Domain Entitiy

Revision ID: 1ccf84938fb2
Revises: 
Create Date: 2022-04-30 19:20:23.224927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1ccf84938fb2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "User",
        sa.Column("id", sa.String(length=64), nullable=False, index=True, unique=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )


def downgrade():
    op.drop_table("User")
