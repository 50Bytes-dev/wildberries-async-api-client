# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_feedbacks_products_rating_top_get200_response import ApiV1FeedbacksProductsRatingTopGet200Response

class TestApiV1FeedbacksProductsRatingTopGet200Response(unittest.TestCase):
    """ApiV1FeedbacksProductsRatingTopGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1FeedbacksProductsRatingTopGet200Response:
        """Test ApiV1FeedbacksProductsRatingTopGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1FeedbacksProductsRatingTopGet200Response`
        """
        model = ApiV1FeedbacksProductsRatingTopGet200Response()
        if include_optional:
            return ApiV1FeedbacksProductsRatingTopGet200Response(
                data = [
                    wildberries_async_api_client.models._api_v1_feedbacks_products_rating_top_get_200_response_data_inner._api_v1_feedbacks_products_rating_top_get_200_response_data_inner(
                        product_max_rating = wildberries_async_api_client.models.product_rating.productRating(
                            nm_id = 56, 
                            imt_id = 56, 
                            valuations_sum = 56, 
                            feedbacks_count = 56, 
                            valuation = 1.337, 
                            product_name = '', 
                            supplier_article = '', 
                            brand_name = '', ), 
                        product_min_rating = wildberries_async_api_client.models.product_rating.productRating(
                            nm_id = 56, 
                            imt_id = 56, 
                            valuations_sum = 56, 
                            feedbacks_count = 56, 
                            valuation = 1.337, 
                            product_name = '', 
                            supplier_article = '', 
                            brand_name = '', ), )
                    ],
                error = True,
                error_text = '',
                additional_errors = [
                    ''
                    ]
            )
        else:
            return ApiV1FeedbacksProductsRatingTopGet200Response(
        )
        """

    def testApiV1FeedbacksProductsRatingTopGet200Response(self):
        """Test ApiV1FeedbacksProductsRatingTopGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
