# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v2_upload_task_post_request import ApiV2UploadTaskPostRequest

class TestApiV2UploadTaskPostRequest(unittest.TestCase):
    """ApiV2UploadTaskPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2UploadTaskPostRequest:
        """Test ApiV2UploadTaskPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2UploadTaskPostRequest`
        """
        model = ApiV2UploadTaskPostRequest()
        if include_optional:
            return ApiV2UploadTaskPostRequest(
                data = [
                    wildberries_async_api_client.models.good.Good(
                        nm_id = 123, 
                        price = 999, 
                        discount = 30, )
                    ]
            )
        else:
            return ApiV2UploadTaskPostRequest(
        )
        """

    def testApiV2UploadTaskPostRequest(self):
        """Test ApiV2UploadTaskPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
