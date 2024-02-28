from sqlalchemy import delete, select, update, delete, Table
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy import select, update
from src.currency.dependencies.repository import IAsyncSession
from src.currency.models import Currency, Rate
from src.currency.dto import CurrencyDTO, RateDTO, LastUpdateDTO


class CurrencyRepository:
    """Репозиторий валюты"""

    model = Currency

    def __init__(self, db_session: IAsyncSession):
        self._session = db_session

    async def last_update(self):
        stmt = select(Rate).order_by(Rate.id.desc())
        rows = await self._session.execute(stmt)
        result = rows.scalars().first()
        return LastUpdateDTO(**result.__dict__)

    async def update_rates(self, dto: [Rate], currency):
        stmt = select(Rate).filter_by(**{'currency': currency.id})
        rows = await self._session.execute(stmt)
        result = rows.scalars().all()
        for obj in result:
            for dto_obj in dto:
                if obj.title == dto_obj.title:
                    obj.value = dto_obj.value
        self._session.add_all(result)
        await self._session.commit()

    async def get_currencie_by_title(self, title: str):
        stmt = select(self.model).filter_by(**{'title': title})
        row = await self._session.execute(stmt)
        result = row.scalar()
        return self._get_dto(result) if result else None

    async def get_target_rate(self, currency: int, title: str):
        stmt = select(Rate).filter_by(**{'currency': currency, 'title': title})
        row = await self._session.execute(stmt)
        result = row.scalar()
        return RateDTO(**result.__dict__)

    async def get_currencies(self):
        stmt = select(self.model)
        rows = await self._session.execute(stmt)
        result = rows.scalars().all()
        return [self._get_dto(row) for row in result] if result else None

    async def create_currencies(self, data: [CurrencyDTO]):
        objects = [self.model(**item.model_dump()) for item in data]
        self._session.add_all(objects)
        await self._session.commit()

    async def create_rates(self, data: [RateDTO]):
        objects = [Rate(**item.model_dump()) for item in data]
        self._session.add_all(objects)
        await self._session.commit()

    def _get_dto(self, row: Currency):
        dct = row.__dict__
        dct.pop('_sa_instance_state')
        return Currency(**dct)

