# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.response_info_advert_type9_united_params_inner_menus_inner import ResponseInfoAdvertType9UnitedParamsInnerMenusInner

class TestResponseInfoAdvertType9UnitedParamsInnerMenusInner(unittest.TestCase):
    """ResponseInfoAdvertType9UnitedParamsInnerMenusInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseInfoAdvertType9UnitedParamsInnerMenusInner:
        """Test ResponseInfoAdvertType9UnitedParamsInnerMenusInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseInfoAdvertType9UnitedParamsInnerMenusInner`
        """
        model = ResponseInfoAdvertType9UnitedParamsInnerMenusInner()
        if include_optional:
            return ResponseInfoAdvertType9UnitedParamsInnerMenusInner(
                id = 56,
                name = ''
            )
        else:
            return ResponseInfoAdvertType9UnitedParamsInnerMenusInner(
        )
        """

    def testResponseInfoAdvertType9UnitedParamsInnerMenusInner(self):
        """Test ResponseInfoAdvertType9UnitedParamsInnerMenusInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
