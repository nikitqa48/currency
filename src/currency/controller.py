from fastapi import APIRouter, HTTPException, Request, Response, HTTPException
from .dto import ConvertDTO
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from src.currency.dependencies.controller import ICurrencyService

router = APIRouter(prefix="", tags=["Currency"])


# @router.get('/init', status_code=HTTP_200_OK)
# async def init(service: ICurrencyService):
#     await service.init_data()


@router.get('/refresh', status_code=HTTP_200_OK)
async def refresh(service: ICurrencyService):
    await service.refresh()


@router.post('/convert', status_code=HTTP_200_OK)
async def convert(dto: ConvertDTO, service: ICurrencyService):
    try:
        return await service.convert(dto)
    except ValueError:
        raise HTTPException(HTTP_400_BAD_REQUEST, 'Нет такой валюты')


@router.get('/last_update', status_code=HTTP_200_OK)
async def last_update(service: ICurrencyService):
    return await service.last_update()


