import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_contentv2tags(api_config_override: Optional[APIConfig] = None) -> ContentV2TagsGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/tags"
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

            return ContentV2TagsGetResponse(**response) if response is not None else ContentV2TagsGetResponse()


async def post_contentv2tag(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ResponseContentError6:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/tag"
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

            return ResponseContentError6(**response) if response is not None else ResponseContentError6()


async def delete_contentv2tagid(
    id: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> Union[ResponseContentError6, ResponseContentError5]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/tag/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
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
                Union[ResponseContentError6, ResponseContentError5](**response)
                if response is not None
                else Union[ResponseContentError6, ResponseContentError5]()
            )


async def patch_contentv2tagid(
    data: Dict[str, Any], id: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> Union[ResponseContentError6, ResponseContentError4]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/tag/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                Union[ResponseContentError6, ResponseContentError4](**response)
                if response is not None
                else Union[ResponseContentError6, ResponseContentError4]()
            )


async def post_contentv2tagnomenclaturelink(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ResponseContentError6:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/tag/nomenclature/link"
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

            return ResponseContentError6(**response) if response is not None else ResponseContentError6()
