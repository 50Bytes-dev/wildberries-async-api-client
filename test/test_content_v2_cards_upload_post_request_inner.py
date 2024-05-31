# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.content_v2_cards_upload_post_request_inner import ContentV2CardsUploadPostRequestInner

class TestContentV2CardsUploadPostRequestInner(unittest.TestCase):
    """ContentV2CardsUploadPostRequestInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentV2CardsUploadPostRequestInner:
        """Test ContentV2CardsUploadPostRequestInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentV2CardsUploadPostRequestInner`
        """
        model = ContentV2CardsUploadPostRequestInner()
        if include_optional:
            return ContentV2CardsUploadPostRequestInner(
                subject_id = 56,
                variants = [
                    wildberries_async_api_client.models._content_v2_cards_upload_post_request_inner_variants_inner._content_v2_cards_upload_post_request_inner_variants_inner(
                        brand = '', 
                        title = '', 
                        description = '', 
                        vendor_code = '', 
                        dimensions = wildberries_async_api_client.models._content_v2_cards_upload_post_request_inner_variants_inner_dimensions._content_v2_cards_upload_post_request_inner_variants_inner_dimensions(
                            length = 56, 
                            width = 56, 
                            height = 56, ), 
                        sizes = [
                            wildberries_async_api_client.models._content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner._content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner(
                                tech_size = '', 
                                wb_size = '', 
                                price = 56, 
                                skus = [
                                    ''
                                    ], )
                            ], 
                        characteristics = [
                            wildberries_async_api_client.models._content_v2_cards_upload_post_request_inner_variants_inner_characteristics_inner._content_v2_cards_upload_post_request_inner_variants_inner_characteristics_inner(
                                id = 56, 
                                value = null, )
                            ], )
                    ]
            )
        else:
            return ContentV2CardsUploadPostRequestInner(
                subject_id = 56,
                variants = [
                    wildberries_async_api_client.models._content_v2_cards_upload_post_request_inner_variants_inner._content_v2_cards_upload_post_request_inner_variants_inner(
                        brand = '', 
                        title = '', 
                        description = '', 
                        vendor_code = '', 
                        dimensions = wildberries_async_api_client.models._content_v2_cards_upload_post_request_inner_variants_inner_dimensions._content_v2_cards_upload_post_request_inner_variants_inner_dimensions(
                            length = 56, 
                            width = 56, 
                            height = 56, ), 
                        sizes = [
                            wildberries_async_api_client.models._content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner._content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner(
                                tech_size = '', 
                                wb_size = '', 
                                price = 56, 
                                skus = [
                                    ''
                                    ], )
                            ], 
                        characteristics = [
                            wildberries_async_api_client.models._content_v2_cards_upload_post_request_inner_variants_inner_characteristics_inner._content_v2_cards_upload_post_request_inner_variants_inner_characteristics_inner(
                                id = 56, 
                                value = null, )
                            ], )
                    ],
        )
        """

    def testContentV2CardsUploadPostRequestInner(self):
        """Test ContentV2CardsUploadPostRequestInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
