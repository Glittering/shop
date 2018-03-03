"""empty message

Revision ID: a23ba58e149c
Revises: 6ddf68b7a120
Create Date: 2018-02-28 16:07:11.698244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a23ba58e149c'
down_revision = '6ddf68b7a120'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('pay', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'pay')
    # ### end Alembic commands ###