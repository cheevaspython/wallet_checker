"""add wallet model

Revision ID: d7a279564b3f
Revises: 
Create Date: 2025-01-21 19:48:03.813755

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d7a279564b3f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "wallets",
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.Column("bandwidth", sa.BigInteger(), nullable=False),
        sa.Column("energy", sa.Integer(), nullable=False),
        sa.Column("balance", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("id", sa.BigInteger(), sa.Identity(always=False), nullable=False),
        sa.Column(
            "created_date",
            sa.DateTime(timezone=True),
            server_default=sa.text("timezone('Europe/Moscow', now())"),
            nullable=False,
        ),
        sa.Column(
            "updated_date",
            sa.DateTime(timezone=True),
            server_default=sa.text("timezone('Europe/Moscow', now())"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_wallets")),
    )
    op.create_index(op.f("ix_wallets_address"), "wallets", ["address"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_wallets_address"), table_name="wallets")
    op.drop_table("wallets")
