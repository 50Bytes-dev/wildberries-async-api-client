# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v3_stocks_warehouse_id_put_request import ApiV3StocksWarehouseIdPutRequest

class TestApiV3StocksWarehouseIdPutRequest(unittest.TestCase):
    """ApiV3StocksWarehouseIdPutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3StocksWarehouseIdPutRequest:
        """Test ApiV3StocksWarehouseIdPutRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3StocksWarehouseIdPutRequest`
        """
        model = ApiV3StocksWarehouseIdPutRequest()
        if include_optional:
            return ApiV3StocksWarehouseIdPutRequest(
                stocks = [
                    wildberries_async_api_client.models._api_v3_stocks__warehouse_id__put_request_stocks_inner._api_v3_stocks__warehouseId__put_request_stocks_inner(
                        sku = 'BarcodeTest123', 
                        amount = 10, )
                    ]
            )
        else:
            return ApiV3StocksWarehouseIdPutRequest(
                stocks = [
                    wildberries_async_api_client.models._api_v3_stocks__warehouse_id__put_request_stocks_inner._api_v3_stocks__warehouseId__put_request_stocks_inner(
                        sku = 'BarcodeTest123', 
                        amount = 10, )
                    ],
        )
        """

    def testApiV3StocksWarehouseIdPutRequest(self):
        """Test ApiV3StocksWarehouseIdPutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
