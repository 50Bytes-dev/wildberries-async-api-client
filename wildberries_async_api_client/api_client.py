import aiohttp
from typing import Optional, Dict, Any
from .api_config import APIConfig
from .models import *


class APIClient:
    """API client for the WB API"""

    def __init__(self, api_config: APIConfig):
        self.api_config = api_config
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_config.get_access_token()}",
        }

    async def _request(self,
                       method: str,
                       path: str,
                       params: Optional[Dict[str, Any]] = None,
                       data: Optional[Dict[str, Any]] = None,
                       return_status: bool = False) -> Dict[str, Any]:
        """Get a response data from the API

        :param method: HTTP method
        :param path: API path
        :param params: Optional parameters
        :param data: Optional data
        :param return_status: Return HTTP status code
        :return: Response
        """
        url = self.api_config.base_path + path
        async with aiohttp.ClientSession() as session:
            async with session.request(
                    method,
                    url,
                    params=params,
                    json=data,
                    headers=self.headers,
            ) as response:
                if return_status:
                    return response.status
                try:
                    response_data = await response.json()
                except aiohttp.ContentTypeError:
                    response_text = await response.text()
                    raise HTTPException(response.status, f"Invalid response from server: {response_text}")
                if response.status != 200:
                    raise HTTPException(response.status, f"{response_data}")
                return response_data

    async def get_new_orders(self) -> NewOrdersGetResponse:
        """Get new orders from API

        :return: List of New orders
        """

        path = "/api/v3/orders/new"
        response_data = await self._request("GET", path)
        return NewOrdersGetResponse(**response_data)

    async def create_new_supply(self, data: Dict[str, Any]) -> NewSuppliesPostResponse:
        """Create new supply

        :param data: Supply data
        :return: Response ID supply
        """

        path = "/api/v3/supplies"
        response_data = await self._request("POST", path, data=data)
        return NewSuppliesPostResponse(**response_data)

    async def get_supply_info(self, supply_id: str) -> Supply:
        """Get supply info

        :param supply_id: Supply id
        :return: Supply info
        """
        path = f"/api/v3/supplies/{supply_id}"
        response_data = await self._request("GET", path)
        return Supply(**response_data)

    async def add_order_to_supply(self, supply_id: str, order_id: int) -> None:  # TODO возврат статуса вместо None
        """Add order to supply

        :param supply_id: Supply id
        :param order_id: Order id
        :return: Status code 204 if success
        """
        path = f"/api/v3/supplies/{supply_id}/orders/{order_id}"
        response_data = await self._request("PATCH", path, return_status=True)
        return response_data

    async def get_product_info(self, barcode: str) -> Card:
        """Get product info by barcode

        :param barcode: Product barcode
        :return: Product info
        """
        path = "/content/v2/get/cards/list"
        params = {'locale': 'ru'}
        data = {
            "settings": {
                "sort": {
                    "ascending": False
                },
                "filter": {
                    "textSearch": barcode,
                    "allowedCategoriesOnly": False,
                    "tagIDs": [],
                    "objectIDs": [],
                    "brands": [],
                    "imtID": 0,
                    "withPhoto": -1
                },
                "cursor": {
                    "limit": 100
                }
            }
        }
        response_data = await self._request("POST", path, params=params, data=data)
        cards = response_data.get('cards', [])
        if cards:
            return Card(**cards[0])
        return None

    async def get_sticker_by_order(self, order_id: int) -> Sticker:
        """Get sticker by order id

        :param order_id: Order id
        :return ResponseStickerModel
        """
        path = '/api/v3/orders/stickers'
        params = {
            'type': 'png',
            'width': 58,
            'height': 40
        }
        payload = {
            'orders': [order_id]
        }
        response_data = await self._request("POST", path, params=params, data=payload)
        stickers = response_data.get('stickers', [])
        if stickers:
            return Sticker(file=stickers[0].get('file'))
        return None



