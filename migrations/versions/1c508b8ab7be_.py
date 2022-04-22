"""empty message

Revision ID: 1c508b8ab7be
Revises: 74791e503a10
Create Date: 2022-04-22 20:17:54.771683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c508b8ab7be'
down_revision = '74791e503a10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fav_planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_planets', sa.Integer(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_planets'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav_planets')
    # ### end Alembic commands ###
