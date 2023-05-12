"""add: longitude and latitude to location

Revision ID: b37f14ddd467
Revises: c1595ba9699a
Create Date: 2023-05-12 07:27:25.046940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b37f14ddd467'
down_revision = 'c1595ba9699a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locations', sa.Column('longitude', sa.Float(), nullable=True))
    op.add_column('locations', sa.Column('latitude', sa.Float(), nullable=True))
    op.add_column('locations', sa.Column('radius', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locations', 'radius')
    op.drop_column('locations', 'latitude')
    op.drop_column('locations', 'longitude')
    # ### end Alembic commands ###
