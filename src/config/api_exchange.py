from typing import Optional
import requests
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class ConfigExchangeApi(BaseSettings):
    EXCHANGE_API_KEY: str

    @property
    def url(self):
        return f'https://api.currencybeacon.com/v1'

    async def request(self, endpoint, params):
        response = requests.get(f'{self.url}/{endpoint}/?api_key={self.EXCHANGE_API_KEY}', params=params)
        data = response.json()
        return data['response']


exchange_api = ConfigExchangeApi()
