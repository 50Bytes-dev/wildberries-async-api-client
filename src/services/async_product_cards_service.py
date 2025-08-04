import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def post_contentv2getcardslist(
    data: Dict[str, Any], locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2GetCardsListPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/get/cards/list"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"locale": locale}

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
                ContentV2GetCardsListPostResponse(**response)
                if response is not None
                else ContentV2GetCardsListPostResponse()
            )


async def get_contentv2cardserrorlist(
    locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2CardsErrorListGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/cards/error/list"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"locale": locale}

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
                ContentV2CardsErrorListGetResponse(**response)
                if response is not None
                else ContentV2CardsErrorListGetResponse()
            )


async def post_contentv2cardsupdate(
    data: List[Dict[str, Any]], api_config_override: Optional[APIConfig] = None
) -> ResponseCardCreate:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/cards/update"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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


async def post_contentv2cardsmoveNm(
    data: Union[RequestMoveNmsImtConn, RequestMoveNmsImtDisconn], api_config_override: Optional[APIConfig] = None
) -> ResponseCardCreate:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/cards/moveNm"
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

            return ResponseCardCreate(**response) if response is not None else ResponseCardCreate()


async def post_contentv2cardsdeletetrash(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ContentV2CardsDeleteTrashPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/cards/delete/trash"
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
                ContentV2CardsDeleteTrashPostResponse(**response)
                if response is not None
                else ContentV2CardsDeleteTrashPostResponse()
            )


async def post_contentv2cardsrecover(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ContentV2CardsRecoverPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/cards/recover"
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
                ContentV2CardsRecoverPostResponse(**response)
                if response is not None
                else ContentV2CardsRecoverPostResponse()
            )


async def post_contentv2getcardstrash(
    data: Dict[str, Any], locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2GetCardsTrashPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://content-api.wildberries.ru"
    path = f"/content/v2/get/cards/trash"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"locale": locale}

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
                ContentV2GetCardsTrashPostResponse(**response)
                if response is not None
                else ContentV2GetCardsTrashPostResponse()
            )
