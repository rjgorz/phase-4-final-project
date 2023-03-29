"""empty message

Revision ID: e401c15c213b
Revises: 713ee12343e8
Create Date: 2023-03-29 13:57:11.157462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e401c15c213b'
down_revision = '713ee12343e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.alter_column('mp3',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.alter_column('mp3',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
