from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from source.db.models import Base
from source.db.models.mixins.create_update import CreateUpdateMixin
from source.db.models.mixins.id_int_pk import IdBigIntPkMixin


class Wallet(
    Base,
    IdBigIntPkMixin,
    CreateUpdateMixin,
):

    address: Mapped[str] = mapped_column(
        String(255),
        index=True,
    )
    free_bandwidth: Mapped[str] = mapped_column(
        String(255),
    )
    total_bandwidth: Mapped[str] = mapped_column(
        String(255),
    )
    total_energy: Mapped[str] = mapped_column(
        String(255),
    )
    balance: Mapped[Decimal] = mapped_column(
        Numeric(20, 2),
    )
