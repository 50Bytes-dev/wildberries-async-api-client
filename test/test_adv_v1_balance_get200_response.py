# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.adv_v1_balance_get200_response import AdvV1BalanceGet200Response

class TestAdvV1BalanceGet200Response(unittest.TestCase):
    """AdvV1BalanceGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvV1BalanceGet200Response:
        """Test AdvV1BalanceGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvV1BalanceGet200Response`
        """
        model = AdvV1BalanceGet200Response()
        if include_optional:
            return AdvV1BalanceGet200Response(
                balance = 56,
                net = 56,
                bonus = 56
            )
        else:
            return AdvV1BalanceGet200Response(
        )
        """

    def testAdvV1BalanceGet200Response(self):
        """Test AdvV1BalanceGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()