"""empty message

Revision ID: ec73371e0efb
Revises: e686fa212efa
Create Date: 2020-05-14 20:25:56.805943

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ec73371e0efb'
down_revision = 'e686fa212efa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
                    sa.Column('operationid', sa.Integer(), nullable=False),
                    sa.Column('operationstatus', sa.Integer(), nullable=False),
                    sa.Column('createdAt', sa.DateTime(), nullable=True),
                    sa.Column('updatedAt', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('operationid'))
    op.create_table(
        'operationsub',
        sa.Column('operationsubid', sa.Integer(), nullable=False),
        sa.Column('operationid', sa.Integer(), nullable=True),
        sa.Column('instanceid', sa.Integer(), nullable=True),
        sa.Column('operationsubtype', sa.String(length=50), nullable=False),
        sa.Column('operationsubdetail', sa.TEXT(), nullable=False),
        sa.Column('operationsubcomment', sa.String(length=250),
                  nullable=False),
        sa.Column('operationsubsequence', sa.Integer(), nullable=False),
        sa.Column('operationsubstatus', sa.Integer(), nullable=False),
        sa.Column('createdAt', sa.DateTime(), nullable=True),
        sa.Column('updatedAt', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ['instanceid'],
            ['instance.instid'],
        ), sa.ForeignKeyConstraint(
            ['operationid'],
            ['operation.operationid'],
        ), sa.PrimaryKeyConstraint('operationsubid'))
    op.create_foreign_key(None, 'saplogin', 'subapp', ['subappid'],
                          ['subappid'])
    op.add_column('subapp',
                  sa.Column('subappmsserv', sa.Integer(), nullable=True))
    op.add_column('subapp', sa.Column('subappguiconn',
                                      sa.TEXT(),
                                      nullable=True))
    op.alter_column('subapp',
                    'createdAt',
                    existing_type=mysql.DATETIME(),
                    nullable=True)
    op.alter_column('subapp',
                    'updatedAt',
                    existing_type=mysql.DATETIME(),
                    nullable=True)
    op.alter_column('user',
                    'createdAt',
                    existing_type=mysql.DATETIME(),
                    nullable=True)
    op.alter_column('user',
                    'updatedAt',
                    existing_type=mysql.DATETIME(),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user',
                    'updatedAt',
                    existing_type=mysql.DATETIME(),
                    nullable=False)
    op.alter_column('user',
                    'createdAt',
                    existing_type=mysql.DATETIME(),
                    nullable=False)
    op.alter_column('subapp',
                    'updatedAt',
                    existing_type=mysql.DATETIME(),
                    nullable=False)
    op.alter_column('subapp',
                    'createdAt',
                    existing_type=mysql.DATETIME(),
                    nullable=False)
    op.drop_column('subapp', 'subappmsserv')
    op.drop_column('subapp', 'subappguiconn')
    op.drop_constraint(None, 'saplogin', type_='foreignkey')
    op.drop_table('operationsub')
    op.drop_table('operation')
    # ### end Alembic commands ###