"""empty message

Revision ID: 7424cd8798eb
Revises:
Create Date: 2024-02-25 11:37:39.823834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7424cd8798eb"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("post", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.VARCHAR(length=21),
            type_=sa.String(length=10),
            existing_nullable=False,
        )

    with op.batch_alter_table("role", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.VARCHAR(length=21),
            type_=sa.String(length=10),
            existing_nullable=False,
        )

    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.VARCHAR(length=21),
            type_=sa.String(length=10),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.String(length=10),
            type_=sa.VARCHAR(length=21),
            existing_nullable=False,
        )

    with op.batch_alter_table("role", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.String(length=10),
            type_=sa.VARCHAR(length=21),
            existing_nullable=False,
        )

    with op.batch_alter_table("post", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.String(length=10),
            type_=sa.VARCHAR(length=21),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
