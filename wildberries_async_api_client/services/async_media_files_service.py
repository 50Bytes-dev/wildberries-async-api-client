import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def post_contentv3mediafile(
    data: Dict[str, Any],
    X_Nm_Id: Optional[str] = None,
    X_Photo_Number: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ContentV3MediaFilePostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v3/media/file"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
        "X-Nm-Id": X_Nm_Id,
        "X-Photo-Number": X_Photo_Number,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "post",
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
                ContentV3MediaFilePostResponse(**response) if response is not None else ContentV3MediaFilePostResponse()
            )


async def post_contentv3mediasave(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ContentV3MediaSavePostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v3/media/save"
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
                ContentV3MediaSavePostResponse(**response) if response is not None else ContentV3MediaSavePostResponse()
            )
