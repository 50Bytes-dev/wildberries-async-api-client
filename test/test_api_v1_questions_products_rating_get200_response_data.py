# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_questions_products_rating_get200_response_data import ApiV1QuestionsProductsRatingGet200ResponseData

class TestApiV1QuestionsProductsRatingGet200ResponseData(unittest.TestCase):
    """ApiV1QuestionsProductsRatingGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1QuestionsProductsRatingGet200ResponseData:
        """Test ApiV1QuestionsProductsRatingGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1QuestionsProductsRatingGet200ResponseData`
        """
        model = ApiV1QuestionsProductsRatingGet200ResponseData()
        if include_optional:
            return ApiV1QuestionsProductsRatingGet200ResponseData(
                products = [
                    wildberries_async_api_client.models._api_v1_questions_products_rating_get_200_response_data_products_inner._api_v1_questions_products_rating_get_200_response_data_products_inner(
                        nm_id = 21573649, 
                        imt_id = 15384080, 
                        product_name = 'Чехол для телефона iPhone 11', 
                        brand_name = 'Case', 
                        questions_count = '11', )
                    ]
            )
        else:
            return ApiV1QuestionsProductsRatingGet200ResponseData(
        )
        """

    def testApiV1QuestionsProductsRatingGet200ResponseData(self):
        """Test ApiV1QuestionsProductsRatingGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
