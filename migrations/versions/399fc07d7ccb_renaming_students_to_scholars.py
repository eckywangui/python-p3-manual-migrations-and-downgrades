"""Renaming students to scholars

Revision ID: 399fc07d7ccb
Revises: 
Create Date: 2023-12-08 17:45:20.995175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '399fc07d7ccb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('students','scholars')

def downgrade() -> None:
    op.rename_table('scholars', 'students')
