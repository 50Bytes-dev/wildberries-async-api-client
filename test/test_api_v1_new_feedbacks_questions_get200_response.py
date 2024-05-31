# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_new_feedbacks_questions_get200_response import ApiV1NewFeedbacksQuestionsGet200Response

class TestApiV1NewFeedbacksQuestionsGet200Response(unittest.TestCase):
    """ApiV1NewFeedbacksQuestionsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1NewFeedbacksQuestionsGet200Response:
        """Test ApiV1NewFeedbacksQuestionsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1NewFeedbacksQuestionsGet200Response`
        """
        model = ApiV1NewFeedbacksQuestionsGet200Response()
        if include_optional:
            return ApiV1NewFeedbacksQuestionsGet200Response(
                data = wildberries_async_api_client.models._api_v1_new_feedbacks_questions_get_200_response_data._api_v1_new_feedbacks_questions_get_200_response_data(
                    has_new_questions = True, 
                    has_new_feedbacks = False, ),
                error = False,
                error_text = '',
                additional_errors = [
                    ''
                    ]
            )
        else:
            return ApiV1NewFeedbacksQuestionsGet200Response(
        )
        """

    def testApiV1NewFeedbacksQuestionsGet200Response(self):
        """Test ApiV1NewFeedbacksQuestionsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
