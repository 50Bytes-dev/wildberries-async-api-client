# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v3_warehouses_post_request import ApiV3WarehousesPostRequest

class TestApiV3WarehousesPostRequest(unittest.TestCase):
    """ApiV3WarehousesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3WarehousesPostRequest:
        """Test ApiV3WarehousesPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3WarehousesPostRequest`
        """
        model = ApiV3WarehousesPostRequest()
        if include_optional:
            return ApiV3WarehousesPostRequest(
                name = 'Склад Коледино',
                office_id = 15
            )
        else:
            return ApiV3WarehousesPostRequest(
                name = 'Склад Коледино',
                office_id = 15,
        )
        """

    def testApiV3WarehousesPostRequest(self):
        """Test ApiV3WarehousesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
