"""empty message

Revision ID: 0287d96c7276
Revises: 11bd8a6531d2
Create Date: 2024-02-26 16:38:38.212559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0287d96c7276"
down_revision = "11bd8a6531d2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("roles_users", schema=None) as batch_op:
        batch_op.alter_column("user_id", existing_type=sa.VARCHAR(), nullable=False)
        batch_op.alter_column("role_id", existing_type=sa.VARCHAR(), nullable=False)
        # batch_op.drop_column("updated_at")
        # batch_op.drop_column("created_at")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("roles_users", schema=None) as batch_op:
        # batch_op.add_column(sa.Column("created_at", sa.DATETIME(), nullable=True))
        # batch_op.add_column(sa.Column("updated_at", sa.DATETIME(), nullable=True))
        batch_op.alter_column("role_id", existing_type=sa.VARCHAR(), nullable=True)
        batch_op.alter_column("user_id", existing_type=sa.VARCHAR(), nullable=True)

    # ### end Alembic commands ###
