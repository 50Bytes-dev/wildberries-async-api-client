# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_list_post200_response_data_inner import ApiV1ListPost200ResponseDataInner

class TestApiV1ListPost200ResponseDataInner(unittest.TestCase):
    """ApiV1ListPost200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ListPost200ResponseDataInner:
        """Test ApiV1ListPost200ResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ListPost200ResponseDataInner`
        """
        model = ApiV1ListPost200ResponseDataInner()
        if include_optional:
            return ApiV1ListPost200ResponseDataInner(
                nm = 56,
                list = [
                    56
                    ]
            )
        else:
            return ApiV1ListPost200ResponseDataInner(
        )
        """

    def testApiV1ListPost200ResponseDataInner(self):
        """Test ApiV1ListPost200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
