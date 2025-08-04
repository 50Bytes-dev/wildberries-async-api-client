import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_apiv1feedbackscount_unanswered(
    api_config_override: Optional[APIConfig] = None,
) -> ApiV1FeedbacksCountUnansweredGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedbacks/count-unanswered"
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
                ApiV1FeedbacksCountUnansweredGetResponse(**response)
                if response is not None
                else ApiV1FeedbacksCountUnansweredGetResponse()
            )


async def get_apiv1feedbackscount(
    dateFrom: Optional[int] = None,
    dateTo: Optional[int] = None,
    isAnswered: Optional[bool] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ApiV1FeedbacksCountGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedbacks/count"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"dateFrom": dateFrom, "dateTo": dateTo, "isAnswered": isAnswered}

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
                ApiV1FeedbacksCountGetResponse(**response) if response is not None else ApiV1FeedbacksCountGetResponse()
            )


async def get_apiv1feedbacks(
    isAnswered: bool,
    take: int,
    skip: int,
    nmId: Optional[int] = None,
    order: Optional[str] = None,
    dateFrom: Optional[int] = None,
    dateTo: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ApiV1FeedbacksGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedbacks"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "isAnswered": isAnswered,
        "nmId": nmId,
        "take": take,
        "skip": skip,
        "order": order,
        "dateFrom": dateFrom,
        "dateTo": dateTo,
    }

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

            return ApiV1FeedbacksGetResponse(**response) if response is not None else ApiV1FeedbacksGetResponse()


async def get_apiv1supplier_valuations(
    X_Locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ApiV1SupplierValuationsGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/supplier-valuations"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "X-Locale": X_Locale,
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
                ApiV1SupplierValuationsGetResponse(**response)
                if response is not None
                else ApiV1SupplierValuationsGetResponse()
            )


async def post_apiv1feedbacksactions(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedbacks/actions"
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
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def post_apiv1feedbacksanswer(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedbacks/answer"
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
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f"{ response }")

            return None


async def patch_apiv1feedbacksanswer(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedbacks/answer"
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


async def post_apiv1feedbacksorderreturn(
    data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> ApiV1FeedbacksOrderReturnPostResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedbacks/order/return"
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
                ApiV1FeedbacksOrderReturnPostResponse(**response)
                if response is not None
                else ApiV1FeedbacksOrderReturnPostResponse()
            )


async def get_apiv1feedback(id: str, api_config_override: Optional[APIConfig] = None) -> ApiV1FeedbackGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedback"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"id": id}

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

            return ApiV1FeedbackGetResponse(**response) if response is not None else ApiV1FeedbackGetResponse()


async def get_apiv1feedbacksarchive(
    take: int,
    skip: int,
    nmId: Optional[int] = None,
    order: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ApiV1FeedbacksArchiveGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/feedbacks/archive"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"nmId": nmId, "take": take, "skip": skip, "order": order}

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
                ApiV1FeedbacksArchiveGetResponse(**response)
                if response is not None
                else ApiV1FeedbacksArchiveGetResponse()
            )
