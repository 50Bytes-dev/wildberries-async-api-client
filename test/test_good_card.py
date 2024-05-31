# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.good_card import GoodCard

class TestGoodCard(unittest.TestCase):
    """GoodCard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoodCard:
        """Test GoodCard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoodCard`
        """
        model = GoodCard()
        if include_optional:
            return GoodCard(
                var_date = '',
                need_refund = True,
                nm_id = 56,
                price = 56,
                price_currency = '',
                rid = '',
                size = '',
                status_id = 56
            )
        else:
            return GoodCard(
        )
        """

    def testGoodCard(self):
        """Test GoodCard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
