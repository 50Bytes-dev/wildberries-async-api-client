import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_apiv1templates(
    templateType: int, api_config_override: Optional[APIConfig] = None
) -> Union[Response200, ResponseErrorTemplate]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/templates"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"templateType": templateType}

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
                Union[Response200, ResponseErrorTemplate](**response)
                if response is not None
                else Union[Response200, ResponseErrorTemplate]()
            )


async def post_apiv1templates(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> Union[PostTemplateOK, ResponseErrorTemplate]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/templates"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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
                Union[PostTemplateOK, ResponseErrorTemplate](**response)
                if response is not None
                else Union[PostTemplateOK, ResponseErrorTemplate]()
            )


async def delete_apiv1templates(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> Union[PatchDelRespOK, ResponseErrorTemplate]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/templates"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("delete", base_path + path, params=query_params, json=data) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                Union[PatchDelRespOK, ResponseErrorTemplate](**response)
                if response is not None
                else Union[PatchDelRespOK, ResponseErrorTemplate]()
            )


async def patch_apiv1templates(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> Union[PatchDelRespOK, ResponseErrorTemplate]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/templates"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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
                Union[PatchDelRespOK, ResponseErrorTemplate](**response)
                if response is not None
                else Union[PatchDelRespOK, ResponseErrorTemplate]()
            )
