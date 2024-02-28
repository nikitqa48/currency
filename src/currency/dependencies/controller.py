from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.currency.service import ExchangeService


ICurrencyService = Annotated[ExchangeService, Depends(ExchangeService)]