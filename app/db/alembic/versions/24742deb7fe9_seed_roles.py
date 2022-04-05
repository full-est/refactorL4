"""seed roles

Revision ID: 24742deb7fe9
Revises: ddb48b496d4d
Create Date: 2022-04-05 09:40:01.545664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24742deb7fe9'
down_revision = 'ddb48b496d4d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("INSERT INTO roles VALUES(1,'owner')")
    op.execute("INSERT INTO roles VALUES(2,'developer')")
    op.execute("INSERT INTO roles VALUES(3,'designer')")
    op.execute("INSERT INTO roles VALUES(4,'tester')")

def downgrade():
    pass
