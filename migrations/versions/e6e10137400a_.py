"""empty message

Revision ID: e6e10137400a
Revises: bd503414c9e9
Create Date: 2018-02-27 16:37:24.811413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6e10137400a'
down_revision = 'bd503414c9e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('school', sa.Column('start', sa.FLOAT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('school', 'start')
    # ### end Alembic commands ###