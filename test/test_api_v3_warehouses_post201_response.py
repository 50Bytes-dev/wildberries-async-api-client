# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v3_warehouses_post201_response import ApiV3WarehousesPost201Response

class TestApiV3WarehousesPost201Response(unittest.TestCase):
    """ApiV3WarehousesPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3WarehousesPost201Response:
        """Test ApiV3WarehousesPost201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3WarehousesPost201Response`
        """
        model = ApiV3WarehousesPost201Response()
        if include_optional:
            return ApiV3WarehousesPost201Response(
                id = 2
            )
        else:
            return ApiV3WarehousesPost201Response(
        )
        """

    def testApiV3WarehousesPost201Response(self):
        """Test ApiV3WarehousesPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
