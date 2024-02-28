from fastapi import APIRouter

from .currency.routes import currency_router


def get_apps_router():
    router = APIRouter()
    router.include_router(currency_router)
    return router