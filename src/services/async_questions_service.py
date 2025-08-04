import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_apiv1new_feedbacks_questions(
    api_config_override: Optional[APIConfig] = None,
) -> ApiV1NewFeedbacksQuestionsGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/new-feedbacks-questions"
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
                ApiV1NewFeedbacksQuestionsGetResponse(**response)
                if response is not None
                else ApiV1NewFeedbacksQuestionsGetResponse()
            )


async def get_apiv1questionscount_unanswered(
    api_config_override: Optional[APIConfig] = None,
) -> ApiV1QuestionsCountUnansweredGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/questions/count-unanswered"
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
                ApiV1QuestionsCountUnansweredGetResponse(**response)
                if response is not None
                else ApiV1QuestionsCountUnansweredGetResponse()
            )


async def get_apiv1questionscount(
    dateFrom: Optional[int] = None,
    dateTo: Optional[int] = None,
    isAnswered: Optional[bool] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ApiV1QuestionsCountGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/questions/count"
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
                ApiV1QuestionsCountGetResponse(**response) if response is not None else ApiV1QuestionsCountGetResponse()
            )


async def get_apiv1questions(
    isAnswered: bool,
    take: int,
    skip: int,
    nmId: Optional[int] = None,
    order: Optional[str] = None,
    dateFrom: Optional[int] = None,
    dateTo: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ApiV1QuestionsGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/questions"
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

            return ApiV1QuestionsGetResponse(**response) if response is not None else ApiV1QuestionsGetResponse()


async def patch_apiv1questions(
    data: Union[Dict[str, Any], Dict[str, Any]], api_config_override: Optional[APIConfig] = None
) -> ApiV1QuestionsPatchResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/questions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data.dict()) as inital_response:
            try:
                response = await inital_response.json()
            except aiohttp.ContentTypeError:
                response_text = await inital_response.text()
                raise HTTPException(inital_response.status, f"Invalid response from server: { response_text}")
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f"{ response }")

            return ApiV1QuestionsPatchResponse(**response) if response is not None else ApiV1QuestionsPatchResponse()


async def get_apiv1question(id: str, api_config_override: Optional[APIConfig] = None) -> ApiV1QuestionGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path or "https://feedbacks-api.wildberries.ru"
    path = f"/api/v1/question"
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

            return ApiV1QuestionGetResponse(**response) if response is not None else ApiV1QuestionGetResponse()
