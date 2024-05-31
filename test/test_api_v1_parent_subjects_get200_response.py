# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_parent_subjects_get200_response import ApiV1ParentSubjectsGet200Response

class TestApiV1ParentSubjectsGet200Response(unittest.TestCase):
    """ApiV1ParentSubjectsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ParentSubjectsGet200Response:
        """Test ApiV1ParentSubjectsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ParentSubjectsGet200Response`
        """
        model = ApiV1ParentSubjectsGet200Response()
        if include_optional:
            return ApiV1ParentSubjectsGet200Response(
                data = [
                    wildberries_async_api_client.models._api_v1_parent_subjects_get_200_response_data_inner._api_v1_parent_subjects_get_200_response_data_inner(
                        subject_id = 1162, 
                        subject_name = 'Строительные инструменты', )
                    ],
                error = False,
                error_text = '',
                additional_errors = [
                    ''
                    ]
            )
        else:
            return ApiV1ParentSubjectsGet200Response(
        )
        """

    def testApiV1ParentSubjectsGet200Response(self):
        """Test ApiV1ParentSubjectsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()