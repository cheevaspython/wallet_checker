from decimal import Decimal

from sqlalchemy import BigInteger, Integer, Numeric, String
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
    bandwidth: Mapped[int] = mapped_column(
        BigInteger(),
    )
    energy: Mapped[int] = mapped_column(
        Integer(),
    )
    balance: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
    )
