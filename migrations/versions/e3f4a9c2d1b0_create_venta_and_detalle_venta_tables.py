"""create venta and detalle_venta tables

Revision ID: e3f4a9c2d1b0
Revises: c79190bd5bd6
Create Date: 2026-03-08 10:40:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e3f4a9c2d1b0"
down_revision = "c79190bd5bd6"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "venta",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("fecha", sa.DateTime(), nullable=False),
        sa.Column("cliente_nombre", sa.String(length=120), nullable=False),
        sa.Column("usuario_id", sa.Integer(), nullable=False),
        sa.Column("total", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.ForeignKeyConstraint(["usuario_id"], ["user.id_usuario"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "detalle_venta",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("venta_id", sa.Integer(), nullable=False),
        sa.Column("producto_id", sa.Integer(), nullable=False),
        sa.Column("cantidad", sa.Integer(), nullable=False),
        sa.Column("precio_unitario", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("subtotal", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.ForeignKeyConstraint(["producto_id"], ["producto.id"]),
        sa.ForeignKeyConstraint(["venta_id"], ["venta.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("detalle_venta")
    op.drop_table("venta")
