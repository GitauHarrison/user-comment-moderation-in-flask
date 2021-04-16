"""add allowed_comment field

Revision ID: de878714b18b
Revises: 585a076d5549
Create Date: 2021-04-15 20:14:28.256057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de878714b18b'
down_revision = '585a076d5549'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('allowed_comment', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'allowed_comment')
    # ### end Alembic commands ###