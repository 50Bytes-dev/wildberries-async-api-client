import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_apiv3ordersnew(api_config_override: Optional[APIConfig] = None) -> ApiV3OrdersNewGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/orders/new"
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

            return ApiV3OrdersNewGetResponse(**response) if response is not None else ApiV3OrdersNewGetResponse()


async def get_apiv3orders(
    limit: Optional[int] = None,
    next: Optional[int] = None,
    dateFrom: Optional[int] = None,
    dateTo: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ApiV3OrdersGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/orders"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {"limit": limit, "next": next, "dateFrom": dateFrom, "dateTo": dateTo}

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

            return ApiV3OrdersGetResponse(**response) if response is not None else ApiV3OrdersGetResponse()


async def post_apiv3ordersstatus(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ApiV3OrdersStatusPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/orders/status"
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
                ApiV3OrdersStatusPostResponse(**response) if response is not None else ApiV3OrdersStatusPostResponse()
            )


async def get_apiv3suppliesordersreshipment(
    api_config_override: Optional[APIConfig] = None,
) -> ApiV3SuppliesOrdersReshipmentGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/orders/reshipment"
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
                ApiV3SuppliesOrdersReshipmentGetResponse(**response)
                if response is not None
                else ApiV3SuppliesOrdersReshipmentGetResponse()
            )


async def patch_apiv3ordersorder_idcancel(
    orderId: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/orders/{orderId}/cancel"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "patch",
            base_path + path,
            params=query_params,
        ) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def post_apiv3ordersstickers(
    data: Dict[str, Any],
    type: Optional[str] = None,
    width: Optional[int] = None,
    height: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ApiV3OrdersStickersPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/orders/stickers"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {"type": type, "width": width, "height": height}

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
                ApiV3OrdersStickersPostResponse(**response)
                if response is not None
                else ApiV3OrdersStickersPostResponse()
            )


async def post_apiv3filesordersexternal_stickers(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ApiV3FilesOrdersExternalStickersPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/files/orders/external-stickers"
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
                ApiV3FilesOrdersExternalStickersPostResponse(**response)
                if response is not None
                else ApiV3FilesOrdersExternalStickersPostResponse()
            )


async def post_apiv3ordersstatushistory(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ApiV3OrdersStatusHistoryPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/orders/status/history"
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
                ApiV3OrdersStatusHistoryPostResponse(**response)
                if response is not None
                else ApiV3OrdersStatusHistoryPostResponse()
            )


async def post_apiv3ordersclient(
    data: OrdersRequestAPI, api_config_override: Optional[APIConfig] = None
) -> CrossborderTurkeyClientInfoResp:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/orders/client"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
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

            return (
                CrossborderTurkeyClientInfoResp(**response)
                if response is not None
                else CrossborderTurkeyClientInfoResp()
            )
