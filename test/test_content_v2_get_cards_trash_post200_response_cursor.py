# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_get_cards_trash_post200_response_cursor import ContentV2GetCardsTrashPost200ResponseCursor

class TestContentV2GetCardsTrashPost200ResponseCursor(unittest.TestCase):
    """ContentV2GetCardsTrashPost200ResponseCursor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2GetCardsTrashPost200ResponseCursor:
        """Test ContentV2GetCardsTrashPost200ResponseCursor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2GetCardsTrashPost200ResponseCursor`
        """
        model = ContentV2GetCardsTrashPost200ResponseCursor()
        if include_optional:
            return ContentV2GetCardsTrashPost200ResponseCursor(
                trashed_at = '',
                nm_id = 56,
                total = 56
            )
        else:
            return ContentV2GetCardsTrashPost200ResponseCursor(
        )
        """

    def testContentV2GetCardsTrashPost200ResponseCursor(self):
        """Test ContentV2GetCardsTrashPost200ResponseCursor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
