from fastapi import APIRouter

from .controller import router


currency_router = APIRouter()
currency_router.include_router(router)
