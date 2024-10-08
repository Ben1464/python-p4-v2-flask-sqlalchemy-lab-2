"""add review

Revision ID: 41011514e299
Revises: 261d9ee54a0a
Create Date: 2024-08-22 09:57:03.469841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41011514e299'
down_revision = '261d9ee54a0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('customers', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('items', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('items', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('price', sa.FLOAT(), nullable=True))
    op.alter_column('items', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('customers', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_table('reviews')
    # ### end Alembic commands ###
