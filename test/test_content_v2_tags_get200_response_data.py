# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_tags_get200_response_data import ContentV2TagsGet200ResponseData

class TestContentV2TagsGet200ResponseData(unittest.TestCase):
    """ContentV2TagsGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2TagsGet200ResponseData:
        """Test ContentV2TagsGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2TagsGet200ResponseData`
        """
        model = ContentV2TagsGet200ResponseData()
        if include_optional:
            return ContentV2TagsGet200ResponseData(
                id = 56,
                color = '',
                name = ''
            )
        else:
            return ContentV2TagsGet200ResponseData(
        )
        """

    def testContentV2TagsGet200ResponseData(self):
        """Test ContentV2TagsGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
