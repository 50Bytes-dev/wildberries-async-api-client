import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_apiv1calendarpromotions(
    startDateTime: str,
    endDateTime: str,
    allPromo: bool,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> PromotionsSuccessResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://dp-calendar-api.wildberries.ru"
    path = f"/api/v1/calendar/promotions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "startDateTime": startDateTime,
        "endDateTime": endDateTime,
        "allPromo": allPromo,
        "limit": limit,
        "offset": offset,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return PromotionsSuccessResponse(**response) if response is not None else PromotionsSuccessResponse()


async def get_apiv1calendarpromotionsdetails(
    promotionIDs: str, api_config_override: Optional[APIConfig] = None
) -> PromotionsGetByIDSuccessResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://dp-calendar-api.wildberries.ru"
    path = f"/api/v1/calendar/promotions/details"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"promotionIDs": promotionIDs}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                PromotionsGetByIDSuccessResponse(**response)
                if response is not None
                else PromotionsGetByIDSuccessResponse()
            )


async def get_apiv1calendarpromotionsnomenclatures(
    promotionID: int,
    inAction: bool,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ResponsePromotionsGoodsLists:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://dp-calendar-api.wildberries.ru"
    path = f"/api/v1/calendar/promotions/nomenclatures"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"promotionID": promotionID, "inAction": inAction, "limit": limit, "offset": offset}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return ResponsePromotionsGoodsLists(**response) if response is not None else ResponsePromotionsGoodsLists()


async def post_apiv1calendarpromotionsupload(
    data: PromotionsSupplierTaskRequest, api_config_override: Optional[APIConfig] = None
) -> UploadSuccessResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://dp-calendar-api.wildberries.ru"
    path = f"/api/v1/calendar/promotions/upload"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return UploadSuccessResponse(**response) if response is not None else UploadSuccessResponse()
