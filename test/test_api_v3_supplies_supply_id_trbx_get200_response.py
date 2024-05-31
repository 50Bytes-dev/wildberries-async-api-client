# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v3_supplies_supply_id_trbx_get200_response import ApiV3SuppliesSupplyIdTrbxGet200Response

class TestApiV3SuppliesSupplyIdTrbxGet200Response(unittest.TestCase):
    """ApiV3SuppliesSupplyIdTrbxGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SuppliesSupplyIdTrbxGet200Response:
        """Test ApiV3SuppliesSupplyIdTrbxGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SuppliesSupplyIdTrbxGet200Response`
        """
        model = ApiV3SuppliesSupplyIdTrbxGet200Response()
        if include_optional:
            return ApiV3SuppliesSupplyIdTrbxGet200Response(
                trbxes = [
                    wildberries_async_api_client.models.supply_trbx.SupplyTrbx(
                        id = 'WB-TRBX-1234567', 
                        orders = [
                            1234567
                            ], )
                    ]
            )
        else:
            return ApiV3SuppliesSupplyIdTrbxGet200Response(
        )
        """

    def testApiV3SuppliesSupplyIdTrbxGet200Response(self):
        """Test ApiV3SuppliesSupplyIdTrbxGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
