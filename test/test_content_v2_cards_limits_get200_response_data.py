# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_cards_limits_get200_response_data import ContentV2CardsLimitsGet200ResponseData

class TestContentV2CardsLimitsGet200ResponseData(unittest.TestCase):
    """ContentV2CardsLimitsGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2CardsLimitsGet200ResponseData:
        """Test ContentV2CardsLimitsGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2CardsLimitsGet200ResponseData`
        """
        model = ContentV2CardsLimitsGet200ResponseData()
        if include_optional:
            return ContentV2CardsLimitsGet200ResponseData(
                free_limits = 56,
                paid_limits = 56
            )
        else:
            return ContentV2CardsLimitsGet200ResponseData(
        )
        """

    def testContentV2CardsLimitsGet200ResponseData(self):
        """Test ContentV2CardsLimitsGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()