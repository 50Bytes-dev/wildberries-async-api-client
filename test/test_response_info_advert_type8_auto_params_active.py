# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.response_info_advert_type8_auto_params_active import ResponseInfoAdvertType8AutoParamsActive

class TestResponseInfoAdvertType8AutoParamsActive(unittest.TestCase):
    """ResponseInfoAdvertType8AutoParamsActive unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseInfoAdvertType8AutoParamsActive:
        """Test ResponseInfoAdvertType8AutoParamsActive
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseInfoAdvertType8AutoParamsActive`
        """
        model = ResponseInfoAdvertType8AutoParamsActive()
        if include_optional:
            return ResponseInfoAdvertType8AutoParamsActive(
                carousel = True,
                recom = True,
                booster = True
            )
        else:
            return ResponseInfoAdvertType8AutoParamsActive(
        )
        """

    def testResponseInfoAdvertType8AutoParamsActive(self):
        """Test ResponseInfoAdvertType8AutoParamsActive"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()