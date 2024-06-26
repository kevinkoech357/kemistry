"""empty message

Revision ID: c98ed6a42381
Revises: 1762ba78f222
Create Date: 2024-04-02 22:06:49.818169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c98ed6a42381"
down_revision = "1762ba78f222"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("post", schema=None) as batch_op:
        batch_op.drop_column("image_url")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("post", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "image_url", sa.VARCHAR(length=150), autoincrement=False, nullable=True
            )
        )

    # ### end Alembic commands ###
