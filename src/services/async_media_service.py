import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_advv1count(api_config_override: Optional[APIConfig] = None) -> AdvV1CountGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://advert-media-api.wildberries.ru"
    path = f"/adv/v1/count"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

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

            return AdvV1CountGetResponse(**response) if response is not None else AdvV1CountGetResponse()


async def get_advv1adverts(
    status: Optional[int] = None,
    type: Optional[int] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    order: Optional[str] = None,
    direction: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Dict[str, Any]]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://advert-media-api.wildberries.ru"
    path = f"/adv/v1/adverts"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "status": status,
        "type": type,
        "limit": limit,
        "offset": offset,
        "order": order,
        "direction": direction,
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

            return response


async def get_advv1advert(id: int, api_config_override: Optional[APIConfig] = None) -> AdvV1AdvertGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://advert-media-api.wildberries.ru"
    path = f"/adv/v1/advert"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"id": id}

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

            return AdvV1AdvertGetResponse(**response) if response is not None else AdvV1AdvertGetResponse()
