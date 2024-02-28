from typing import Annotated

from fastapi import Depends
from src.currency.repository import CurrencyRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.api_exchange import ConfigExchangeApi

from src.config.db_helper import db_helper


ICurrencyRepository = Annotated[CurrencyRepository, Depends(CurrencyRepository)]
IConfigDepends = Annotated[ConfigExchangeApi, Depends(ConfigExchangeApi)]
