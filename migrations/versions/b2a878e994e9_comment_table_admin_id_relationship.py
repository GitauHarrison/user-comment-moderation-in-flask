"""comment table admin_id relationship

Revision ID: b2a878e994e9
Revises: d27105d2cdc3
Create Date: 2021-04-21 04:14:14.607153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2a878e994e9'
down_revision = 'd27105d2cdc3'
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