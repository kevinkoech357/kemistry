"""Modify Posts table, tag column

Revision ID: 6ec2230c6bd9
Revises: 2385e51c7bee
Create Date: 2024-04-02 22:52:33.885789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6ec2230c6bd9"
down_revision = "2385e51c7bee"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("post", schema=None) as batch_op:
        batch_op.alter_column(
            "tag", existing_type=sa.VARCHAR(length=255), nullable=False
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("post", schema=None) as batch_op:
        batch_op.alter_column(
            "tag", existing_type=sa.VARCHAR(length=255), nullable=True
        )

    # ### end Alembic commands ###