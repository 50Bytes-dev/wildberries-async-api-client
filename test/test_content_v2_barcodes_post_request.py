# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_barcodes_post_request import ContentV2BarcodesPostRequest

class TestContentV2BarcodesPostRequest(unittest.TestCase):
    """ContentV2BarcodesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2BarcodesPostRequest:
        """Test ContentV2BarcodesPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2BarcodesPostRequest`
        """
        model = ContentV2BarcodesPostRequest()
        if include_optional:
            return ContentV2BarcodesPostRequest(
                count = 100
            )
        else:
            return ContentV2BarcodesPostRequest(
        )
        """

    def testContentV2BarcodesPostRequest(self):
        """Test ContentV2BarcodesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()