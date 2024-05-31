# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_get_cards_trash_post_request_settings import ContentV2GetCardsTrashPostRequestSettings

class TestContentV2GetCardsTrashPostRequestSettings(unittest.TestCase):
    """ContentV2GetCardsTrashPostRequestSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2GetCardsTrashPostRequestSettings:
        """Test ContentV2GetCardsTrashPostRequestSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2GetCardsTrashPostRequestSettings`
        """
        model = ContentV2GetCardsTrashPostRequestSettings()
        if include_optional:
            return ContentV2GetCardsTrashPostRequestSettings(
                sort = wildberries_async_api_client.models._content_v2_get_cards_trash_post_request_settings_sort._content_v2_get_cards_trash_post_request_settings_sort(
                    ascending = True, ),
                cursor = wildberries_async_api_client.models._content_v2_get_cards_trash_post_request_settings_cursor._content_v2_get_cards_trash_post_request_settings_cursor(
                    limit = 56, ),
                filter = wildberries_async_api_client.models._content_v2_get_cards_trash_post_request_settings_filter._content_v2_get_cards_trash_post_request_settings_filter(
                    text_search = '', )
            )
        else:
            return ContentV2GetCardsTrashPostRequestSettings(
        )
        """

    def testContentV2GetCardsTrashPostRequestSettings(self):
        """Test ContentV2GetCardsTrashPostRequestSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
