"""empty message

Revision ID: 5219a93d4c03
Revises: ac1704a12a11
Create Date: 2019-07-18 16:45:05.197765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5219a93d4c03'
down_revision = 'ac1704a12a11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###