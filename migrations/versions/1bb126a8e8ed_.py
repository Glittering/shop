"""empty message

Revision ID: 1bb126a8e8ed
Revises: 442426be7e30
Create Date: 2018-02-03 20:16:22.570037

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1bb126a8e8ed'
down_revision = '442426be7e30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('add_time', sa.DATETIME(), nullable=True))
    op.add_column('goods', sa.Column('add_time', sa.DATETIME(), nullable=True))
    op.drop_column('goods', 'ad_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('ad_time', mysql.DATETIME(), nullable=True))
    op.drop_column('goods', 'add_time')
    op.drop_column('address', 'add_time')
    # ### end Alembic commands ###
