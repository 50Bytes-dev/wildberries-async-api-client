# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_questions_count_get200_response import ApiV1QuestionsCountGet200Response

class TestApiV1QuestionsCountGet200Response(unittest.TestCase):
    """ApiV1QuestionsCountGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1QuestionsCountGet200Response:
        """Test ApiV1QuestionsCountGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1QuestionsCountGet200Response`
        """
        model = ApiV1QuestionsCountGet200Response()
        if include_optional:
            return ApiV1QuestionsCountGet200Response(
                data = 77,
                error = False,
                error_text = '',
                additional_errors = [
                    ''
                    ]
            )
        else:
            return ApiV1QuestionsCountGet200Response(
        )
        """

    def testApiV1QuestionsCountGet200Response(self):
        """Test ApiV1QuestionsCountGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
