# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_cards_upload_add_post_request_cards_to_add_inner_sizes_inner import ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner

class TestContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner(unittest.TestCase):
    """ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner:
        """Test ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner`
        """
        model = ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner()
        if include_optional:
            return ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner(
                tech_size = '',
                wb_size = '',
                price = 56,
                skus = [
                    ''
                    ]
            )
        else:
            return ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner(
        )
        """

    def testContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner(self):
        """Test ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
