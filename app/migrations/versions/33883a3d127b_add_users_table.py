"""add users table

Revision ID: 33883a3d127b
Revises: 
Create Date: 2024-01-09 12:15:50.670153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33883a3d127b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=64), nullable=True))
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('name')
        batch_op.drop_column('id')

    # ### end Alembic commands ###
