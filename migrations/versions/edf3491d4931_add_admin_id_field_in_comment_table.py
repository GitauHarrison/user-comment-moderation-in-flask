"""add admin_id field in comment table

Revision ID: edf3491d4931
Revises: 845d08b8b634
Create Date: 2021-04-21 04:03:44.581855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edf3491d4931'
down_revision = '845d08b8b634'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'admin', ['admin_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('admin_id')

    # ### end Alembic commands ###