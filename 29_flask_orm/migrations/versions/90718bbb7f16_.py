"""empty message

Revision ID: 90718bbb7f16
Revises: 803908dbead7
Create Date: 2024-08-21 20:43:36.054177

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '90718bbb7f16'
down_revision = '803908dbead7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.Text(), nullable=True))
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('content',
               existing_type=mysql.TEXT(),
               nullable=False)
        batch_op.alter_column('author',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.alter_column('author',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('content',
               existing_type=mysql.TEXT(),
               nullable=True)
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('image')

    # ### end Alembic commands ###
