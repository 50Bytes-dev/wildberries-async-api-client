# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.good_buffer_history import GoodBufferHistory

class TestGoodBufferHistory(unittest.TestCase):
    """GoodBufferHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoodBufferHistory:
        """Test GoodBufferHistory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoodBufferHistory`
        """
        model = GoodBufferHistory()
        if include_optional:
            return GoodBufferHistory(
                nm_id = 544833232,
                vendor_code = '34552332',
                size_id = 54483342,
                tech_size_name = 'XXL',
                price = 1500,
                currency_iso_code4217 = 'RUB',
                discount = 25,
                status = 1,
                error_text = ''
            )
        else:
            return GoodBufferHistory(
        )
        """

    def testGoodBufferHistory(self):
        """Test GoodBufferHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()