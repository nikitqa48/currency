from pydantic import BaseModel
from datetime import datetime, date


class CurrencyDTO(BaseModel):
    """Базовая DTO Pydantic.
    С поддержкой ORM
    """
    id: int | None = None
    code: int
    title: str

    class Config:
        from_attributes = True


class LastUpdateDTO(BaseModel):
    updated_at: datetime


class RateDTO(BaseModel):
    value: float
    title: str
    currency: int

    class Config:
        from_attributes = True


class ConvertDTO(BaseModel):
    original: str
    target: str
    amount: int