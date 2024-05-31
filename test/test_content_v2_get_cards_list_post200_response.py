# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_get_cards_list_post200_response import ContentV2GetCardsListPost200Response

class TestContentV2GetCardsListPost200Response(unittest.TestCase):
    """ContentV2GetCardsListPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2GetCardsListPost200Response:
        """Test ContentV2GetCardsListPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2GetCardsListPost200Response`
        """
        model = ContentV2GetCardsListPost200Response()
        if include_optional:
            return ContentV2GetCardsListPost200Response(
                cards = [
                    wildberries_async_api_client.models._content_v2_get_cards_list_post_200_response_cards_inner._content_v2_get_cards_list_post_200_response_cards_inner(
                        nm_id = 56, 
                        imt_id = 56, 
                        nm_uuid = '', 
                        subject_id = 56, 
                        vendor_code = '', 
                        subject_name = '', 
                        brand = '', 
                        title = '', 
                        photos = [
                            wildberries_async_api_client.models._content_v2_get_cards_list_post_200_response_cards_inner_photos_inner._content_v2_get_cards_list_post_200_response_cards_inner_photos_inner(
                                big = '', 
                                c246x328 = '', 
                                c516x688 = '', 
                                square = '', 
                                tm = '', )
                            ], 
                        video = '', 
                        dimensions = wildberries_async_api_client.models._content_v2_get_cards_list_post_200_response_cards_inner_dimensions._content_v2_get_cards_list_post_200_response_cards_inner_dimensions(
                            length = 56, 
                            width = 56, 
                            height = 56, ), 
                        characteristics = [
                            wildberries_async_api_client.models._content_v2_get_cards_list_post_200_response_cards_inner_characteristics_inner._content_v2_get_cards_list_post_200_response_cards_inner_characteristics_inner(
                                id = 56, 
                                name = '', 
                                value = null, )
                            ], 
                        sizes = [
                            wildberries_async_api_client.models._content_v2_get_cards_list_post_200_response_cards_inner_sizes_inner._content_v2_get_cards_list_post_200_response_cards_inner_sizes_inner(
                                chrt_id = 56, 
                                tech_size = '', 
                                wb_size = '', 
                                skus = [
                                    '12345Ejf5'
                                    ], )
                            ], 
                        tags = [
                            wildberries_async_api_client.models._content_v2_get_cards_list_post_200_response_cards_inner_tags_inner._content_v2_get_cards_list_post_200_response_cards_inner_tags_inner(
                                id = 56, 
                                name = '', 
                                color = '', )
                            ], 
                        created_at = '', 
                        updated_at = '', )
                    ],
                cursor = wildberries_async_api_client.models._content_v2_get_cards_list_post_200_response_cursor._content_v2_get_cards_list_post_200_response_cursor(
                    updated_at = '', 
                    nm_id = 56, 
                    total = 56, )
            )
        else:
            return ContentV2GetCardsListPost200Response(
        )
        """

    def testContentV2GetCardsListPost200Response(self):
        """Test ContentV2GetCardsListPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()