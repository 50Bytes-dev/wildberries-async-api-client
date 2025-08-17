import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_advv1promotioncount(api_config_override: Optional[APIConfig] = None) -> AdvV1PromotionCountGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://advert-api.wildberries.ru"
    path = f"/adv/v1/promotion/count"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
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

            return (
                AdvV1PromotionCountGetResponse(**response) if response is not None else AdvV1PromotionCountGetResponse()
            )


async def post_advv1promotionadverts(
    data: List[int],
    status: Optional[int] = None,
    type: Optional[int] = None,
    order: Optional[str] = None,
    direction: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Union[ResponseInfoAdvert, ResponseInfoAdvertType8, ResponseInfoAdvertType9]]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://advert-api.wildberries.ru"
    path = f"/adv/v1/promotion/adverts"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {"status": status, "type": type, "order": order, "direction": direction}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "post", base_path + path, params=query_params, json=[i.dict() for i in data]
        ) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return response
