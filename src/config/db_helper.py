from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, async_sessionmaker, create_async_engine

from .db_config import settings_db


class DatabaseHelper:
    """Класс для работы с базой данных"""

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)

        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    def get_scope_session(self):
        return async_scoped_session(session_factory=self.session_factory, scopefunc=current_task)

    async def get_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.session_factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()


db_helper = DatabaseHelper(settings_db.database_url, settings_db.DB_ECHO_LOG)