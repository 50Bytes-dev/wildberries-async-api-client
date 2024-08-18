import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_apiv3supplies(
    limit: int, next: int, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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

    base_path = api_config.base_path
    path = f"/api/v3/supplies"
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
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f"{ response }")

            return ApiV3SuppliesPostResponse(**response) if response is not None else ApiV3SuppliesPostResponse()


async def patch_apiv3suppliessupplyIdordersorderId(
    supplyId: str, orderId: int, api_config_override: Optional[APIConfig] = None
) -> bool:  # TODO return bool - True or False
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/orders/{orderId}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "patch",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status == 204:
                return True
            # TODO исправить генератор - тут в случае успеха ответ 204 - и не нужно  овить ошибку aiohttp.ContentTypeError
            response_text = await initial_response.text()
            raise HTTPException(inital_response.status, f"{ response }")

    return False


async def get_apiv3suppliessupplyId(supplyId: str, api_config_override: Optional[APIConfig] = None) -> Supply:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}"
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

            return Supply(**response) if response is not None else Supply()


async def delete_apiv3suppliessupplyId(supplyId: str, api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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


async def get_apiv3suppliessupplyIdorders(
    supplyId: str, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdOrdersGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/orders"
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

            return (
                ApiV3SuppliesSupplyIdOrdersGetResponse(**response)
                if response is not None
                else ApiV3SuppliesSupplyIdOrdersGetResponse()
            )


async def patch_apiv3suppliessupplyIddeliver(supplyId: str, api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/deliver"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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


async def get_apiv3suppliessupplyIdbarcode(
    supplyId: str, type: str, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdBarcodeGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/barcode"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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


async def get_apiv3suppliessupplyIdtrbx(
    supplyId: str, api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdTrbxGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/trbx"
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

            return (
                ApiV3SuppliesSupplyIdTrbxGetResponse(**response)
                if response is not None
                else ApiV3SuppliesSupplyIdTrbxGetResponse()
            )


async def post_apiv3suppliessupplyIdtrbx(
    supplyId: str, data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdTrbxPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/trbx"
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
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f"{ response }")

            return (
                ApiV3SuppliesSupplyIdTrbxPostResponse(**response)
                if response is not None
                else ApiV3SuppliesSupplyIdTrbxPostResponse()
            )


async def delete_apiv3suppliessupplyIdtrbx(
    supplyId: str, data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/trbx"
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
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def patch_apiv3suppliessupplyIdtrbxtrbxId(
    supplyId: str, trbxId: str, data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/trbx/{trbxId}"
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
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def delete_apiv3suppliessupplyIdtrbxtrbxIdordersorderId(
    supplyId: str, trbxId: str, orderId: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/trbx/{trbxId}/orders/{orderId}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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


async def post_apiv3suppliessupplyIdtrbxstickers(
    supplyId: str, type: str, data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ApiV3SuppliesSupplyIdTrbxStickersPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/v3/supplies/{supplyId}/trbx/stickers"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
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
