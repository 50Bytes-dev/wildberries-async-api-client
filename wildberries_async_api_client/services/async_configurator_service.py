import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_contentv2objectparentall(
    locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2ObjectParentAllGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/object/parent/all"
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
                ContentV2ObjectParentAllGetResponse(**response)
                if response is not None
                else ContentV2ObjectParentAllGetResponse()
            )


async def get_contentv2objectall(
    name: Optional[str] = None,
    limit: Optional[int] = None,
    locale: Optional[str] = None,
    offset: Optional[int] = None,
    parentID: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ContentV2ObjectAllGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/object/all"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "name": name,
        "limit": limit,
        "locale": locale,
        "offset": offset,
        "parentID": parentID,
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

            return (
                ContentV2ObjectAllGetResponse(**response) if response is not None else ContentV2ObjectAllGetResponse()
            )


async def get_contentv2objectcharcssubjectId(
    subjectId: int, locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2ObjectCharcsSubjectIdGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/object/charcs/{subjectId}"
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
                ContentV2ObjectCharcsSubjectIdGetResponse(**response)
                if response is not None
                else ContentV2ObjectCharcsSubjectIdGetResponse()
            )


async def get_contentv2directorycolors(
    locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2DirectoryColorsGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/directory/colors"
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
                ContentV2DirectoryColorsGetResponse(**response)
                if response is not None
                else ContentV2DirectoryColorsGetResponse()
            )


async def get_contentv2directorykinds(
    locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2DirectoryKindsGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/directory/kinds"
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
                ContentV2DirectoryKindsGetResponse(**response)
                if response is not None
                else ContentV2DirectoryKindsGetResponse()
            )


async def get_contentv2directorycountries(
    locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2DirectoryCountriesGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/directory/countries"
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
                ContentV2DirectoryCountriesGetResponse(**response)
                if response is not None
                else ContentV2DirectoryCountriesGetResponse()
            )


async def get_contentv2directoryseasons(
    locale: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> ContentV2DirectorySeasonsGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/directory/seasons"
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
                ContentV2DirectorySeasonsGetResponse(**response)
                if response is not None
                else ContentV2DirectorySeasonsGetResponse()
            )


async def get_contentv2directorytnved(
    subjectID: int,
    search: Optional[int] = None,
    locale: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> ContentV2DirectoryTnvedGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/directory/tnved"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"subjectID": subjectID, "search": search, "locale": locale}

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
                ContentV2DirectoryTnvedGetResponse(**response)
                if response is not None
                else ContentV2DirectoryTnvedGetResponse()
            )


async def get_contentv2directoryvat(
    locale: str, api_config_override: Optional[APIConfig] = None
) -> ContentV2DirectoryVatGetResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/content/v2/directory/vat"
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
                ContentV2DirectoryVatGetResponse(**response)
                if response is not None
                else ContentV2DirectoryVatGetResponse()
            )
