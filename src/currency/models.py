from sqlalchemy import Boolean, String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from src.base_model import Base


class Rate(Base):
    """Модель курса

    :param title: название валюты
    :param code: код валюты
    :param currency: валюта
    """

    __tablename__ = "rate"

    value: Mapped[float] = mapped_column(Float, nullable=False)
    title: Mapped[str] = mapped_column(String(20))
    currency: Mapped[int] = mapped_column(ForeignKey('currency.id'), nullable=False)


class Currency(Base):
    """Модель валюты

    :param title: название валюты
    :param code: код валюты
    """

    __tablename__ = "currency"

    title: Mapped[str] = mapped_column(String(20))
    code: Mapped[str] = mapped_column(Integer)

