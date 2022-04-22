"""empty message

Revision ID: 9bd66aa4e229
Revises: 
Create Date: 2022-04-21 22:49:45.343719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bd66aa4e229'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('mass', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.Column('gravity', sa.String(length=120), nullable=True),
    sa.Column('residents', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['residents'], ['people.uid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('user')
    op.drop_table('people')
    # ### end Alembic commands ###
