# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v2_history_tasks_get4_xx_response import ApiV2HistoryTasksGet4XXResponse

class TestApiV2HistoryTasksGet4XXResponse(unittest.TestCase):
    """ApiV2HistoryTasksGet4XXResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2HistoryTasksGet4XXResponse:
        """Test ApiV2HistoryTasksGet4XXResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2HistoryTasksGet4XXResponse`
        """
        model = ApiV2HistoryTasksGet4XXResponse()
        if include_optional:
            return ApiV2HistoryTasksGet4XXResponse(
                data = None,
                error = True,
                error_text = 'Unknown error'
            )
        else:
            return ApiV2HistoryTasksGet4XXResponse(
        )
        """

    def testApiV2HistoryTasksGet4XXResponse(self):
        """Test ApiV2HistoryTasksGet4XXResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
