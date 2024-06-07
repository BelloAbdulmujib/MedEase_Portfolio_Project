"""empty message

Revision ID: 7d5c1c6ea25a
Revises: ab22f83945c8
Create Date: 2024-06-06 23:20:46.452462

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7d5c1c6ea25a'
down_revision = 'ab22f83945c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.drop_constraint('fk_appointment_patient', type_='foreignkey')
        batch_op.drop_column('patient_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('patient_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('fk_appointment_patient', 'patient', ['patient_id'], ['id'])

    # ### end Alembic commands ###
