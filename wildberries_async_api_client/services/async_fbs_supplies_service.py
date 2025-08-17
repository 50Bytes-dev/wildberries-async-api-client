import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_apiv3supplies(
    limit: Optional[int] = None, next: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {"limit": limit, "next": next}

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

            return ApiV3SuppliesGetResponse(**response) if response is not None else ApiV3SuppliesGetResponse()


async def post_apiv3supplies(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies"
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
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f"{ response }")

            return ApiV3SuppliesPostResponse(**response) if response is not None else ApiV3SuppliesPostResponse()


async def patch_apiv3suppliessupply_idordersorder_id(
    supplyId: Optional[str] = None, orderId: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/orders/{orderId}"
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


async def get_apiv3suppliessupply_id(
    supplyId: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> Supply:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}"
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

            return Supply(**response) if response is not None else Supply()


async def delete_apiv3suppliessupply_id(
    supplyId: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}"
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
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def get_apiv3suppliessupply_idorders(
    supplyId: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdOrdersGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/orders"
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
                ApiV3SuppliesSupplyIdOrdersGetResponse(**response)
                if response is not None
                else ApiV3SuppliesSupplyIdOrdersGetResponse()
            )


async def patch_apiv3suppliessupply_iddeliver(
    supplyId: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/deliver"
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


async def get_apiv3suppliessupply_idbarcode(
    supplyId: Optional[str] = None, type: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdBarcodeGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/barcode"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {"type": type}

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
                ApiV3SuppliesSupplyIdBarcodeGetResponse(**response)
                if response is not None
                else ApiV3SuppliesSupplyIdBarcodeGetResponse()
            )


async def get_apiv3suppliessupply_idtrbx(
    supplyId: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdTrbxGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/trbx"
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
                ApiV3SuppliesSupplyIdTrbxGetResponse(**response)
                if response is not None
                else ApiV3SuppliesSupplyIdTrbxGetResponse()
            )


async def post_apiv3suppliessupply_idtrbx(
    data: Dict[str, Any], supplyId: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdTrbxPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/trbx"
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
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                ApiV3SuppliesSupplyIdTrbxPostResponse(**response)
                if response is not None
                else ApiV3SuppliesSupplyIdTrbxPostResponse()
            )


async def delete_apiv3suppliessupply_idtrbx(
    data: Dict[str, Any], supplyId: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/trbx"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
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
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def patch_apiv3suppliessupply_idtrbxtrbx_id(
    data: Dict[str, Any],
    supplyId: Optional[str] = None,
    trbxId: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/trbx/{trbxId}"
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
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def delete_apiv3suppliessupply_idtrbxtrbx_idordersorder_id(
    supplyId: Optional[str] = None,
    trbxId: Optional[str] = None,
    orderId: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/trbx/{trbxId}/orders/{orderId}"
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
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def post_apiv3suppliessupply_idtrbxstickers(
    data: Dict[str, Any],
    supplyId: Optional[str] = None,
    type: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ApiV3SuppliesSupplyIdTrbxStickersPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://marketplace-api.wildberries.ru"
    path = f"/api/v3/supplies/{supplyId}/trbx/stickers"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{ api_config.access_token }",
    }

    query_params: Dict[str, Any] = {"type": type}

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
                ApiV3SuppliesSupplyIdTrbxStickersPostResponse(**response)
                if response is not None
                else ApiV3SuppliesSupplyIdTrbxStickersPostResponse()
            )
