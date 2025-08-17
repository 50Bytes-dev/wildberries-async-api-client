import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_contentv2cardslimits(api_config_override: Optional[APIConfig] = None) -> ContentV2CardsLimitsGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/cards/limits"
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
                ContentV2CardsLimitsGetResponse(**response)
                if response is not None
                else ContentV2CardsLimitsGetResponse()
            )


async def post_contentv2barcodes(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ContentV2BarcodesPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/barcodes"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                ContentV2BarcodesPostResponse(**response) if response is not None else ContentV2BarcodesPostResponse()
            )


async def post_contentv2cardsupload(
    data: List[Dict[str, Any]], api_config_override: Optional[APIConfig] = None
) -> ResponseCardCreate:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/cards/upload"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {}

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

            return ResponseCardCreate(**response) if response is not None else ResponseCardCreate()


async def post_contentv2cardsuploadadd(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ResponseCardCreate:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/cards/upload/add"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return ResponseCardCreate(**response) if response is not None else ResponseCardCreate()
