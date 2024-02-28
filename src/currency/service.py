from .dependencies.services import ICurrencyRepository, ConfigExchangeApi
from src.config.api_exchange import exchange_api
from .dto import CurrencyDTO, RateDTO, ConvertDTO
import requests
import json


class ExchangeService:

    def __init__(self, currency_repository: ICurrencyRepository):
        self.currency_repository = currency_repository
        self.api = exchange_api

    async def init_data(self):
        await self._init_currencies()
        currencies = await self.currency_repository.get_currencies()
        [await self._init_rates(currencie) for currencie in currencies]

    async def _init_rates(self, currency: CurrencyDTO):
        endpoint = 'latest'
        params = {'base': currency.title}
        response = await self.api.request(endpoint, params)
        if not isinstance(response['rates'], list):
            rates_data = response['rates'].items()
            rates_dto = [RateDTO(title=data[0], value=data[1], currency=currency.id) for data in rates_data]
            await self.currency_repository.create_rates(rates_dto)

    async def _init_currencies(self):
        endpoint = 'currencies'
        result = await self.api.request(endpoint, params=None)
        data = [CurrencyDTO(code=item['code'], title=item['short_code']) for item in result]
        await self.currency_repository.create_currencies(data)
        return data

    async def _refresh_currency_rate(self, currency: CurrencyDTO):
        endpoint = 'latest'
        params = {'base': currency.title}
        response = await self.api.request(endpoint, params)
        if not isinstance(response['rates'], list):
            rates_data = response['rates'].items()
            rates_dto = [RateDTO(title=data[0], value=data[1], currency=currency.id) for data in rates_data]
            await self.currency_repository.update_rates(rates_dto, currency)

    async def refresh(self):
        currencies = await self.currency_repository.get_currencies()
        [await self._refresh_currency_rate(currencie) for currencie in currencies]

    async def convert(self, dto: ConvertDTO):
        currency = await self.currency_repository.get_currencie_by_title(dto.original.upper())
        if not currency:
            raise ValueError('Нет такой валюты, введите короткое название, например USD')
        rate = await self.currency_repository.get_target_rate(currency.id, dto.target.upper())
        return dto.amount * rate.value

    async def last_update(self):
        result = await self.currency_repository.last_update()
        return result.updated_at



