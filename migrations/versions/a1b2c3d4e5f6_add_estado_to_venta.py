"""add estado and fecha_confirmacion to venta

Revision ID: a1b2c3d4e5f6
Revises: e3f4a9c2d1b0
Create Date: 2026-03-08 10:41:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a1b2c3d4e5f6"
down_revision = "e3f4a9c2d1b0"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "venta",
        sa.Column("estado", sa.String(length=20), nullable=False, server_default="borrador"),
    )
    op.add_column(
        "venta",
        sa.Column("fecha_confirmacion", sa.DateTime(), nullable=True),
    )


def downgrade():
    op.drop_column("venta", "fecha_confirmacion")
    op.drop_column("venta", "estado")
