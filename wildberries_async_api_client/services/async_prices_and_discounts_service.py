import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def post_apiv2uploadtask(
    data: SupplierTaskRequest, api_config_override: Optional[APIConfig] = None
) -> SuccessTaskResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/upload/task"
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

            return SuccessTaskResponse(**response) if response is not None else SuccessTaskResponse()


async def post_apiv2uploadtasksize(
    data: SupplierTaskRequestSize, api_config_override: Optional[APIConfig] = None
) -> SuccessTaskResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/upload/task/size"
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

            return SuccessTaskResponse(**response) if response is not None else SuccessTaskResponse()


async def post_apiv2uploadtaskclub_discount(
    data: SupplierTaskRequestClubDisc, api_config_override: Optional[APIConfig] = None
) -> SuccessTaskResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/upload/task/club-discount"
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

            return SuccessTaskResponse(**response) if response is not None else SuccessTaskResponse()


async def get_apiv2historytasks(uploadID: int, api_config_override: Optional[APIConfig] = None) -> ResponseTaskHistory:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/history/tasks"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"uploadID": uploadID}

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

            return ResponseTaskHistory(**response) if response is not None else ResponseTaskHistory()


async def get_apiv2historygoodstask(
    limit: int, uploadID: int, offset: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> ResponseGoodHistories:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/history/goods/task"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"limit": limit, "offset": offset, "uploadID": uploadID}

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

            return ResponseGoodHistories(**response) if response is not None else ResponseGoodHistories()


async def get_apiv2buffertasks(uploadID: int, api_config_override: Optional[APIConfig] = None) -> ResponseTaskBuffer:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/buffer/tasks"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"uploadID": uploadID}

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

            return ResponseTaskBuffer(**response) if response is not None else ResponseTaskBuffer()


async def get_apiv2buffergoodstask(
    limit: int, uploadID: int, offset: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> ResponseGoodBufferHistories:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/buffer/goods/task"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"limit": limit, "offset": offset, "uploadID": uploadID}

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

            return ResponseGoodBufferHistories(**response) if response is not None else ResponseGoodBufferHistories()


async def get_apiv2listgoodsfilter(
    limit: int,
    offset: Optional[int] = None,
    filterNmID: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ResponseGoodsLists:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/list/goods/filter"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"limit": limit, "offset": offset, "filterNmID": filterNmID}

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

            return ResponseGoodsLists(**response) if response is not None else ResponseGoodsLists()


async def get_apiv2listgoodssizenm(
    limit: int, nmID: int, offset: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> ResponseSizeLists:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/list/goods/size/nm"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"limit": limit, "offset": offset, "nmID": nmID}

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

            return ResponseSizeLists(**response) if response is not None else ResponseSizeLists()


async def get_apiv2quarantinegoods(
    limit: int, offset: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> ResponseQuarantineGoods:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://discounts-prices-api.wildberries.ru"
    path = f"/api/v2/quarantine/goods"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"limit": limit, "offset": offset}

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

            return ResponseQuarantineGoods(**response) if response is not None else ResponseQuarantineGoods()
