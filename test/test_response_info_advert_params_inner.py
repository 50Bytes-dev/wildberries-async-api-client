# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.response_info_advert_params_inner import ResponseInfoAdvertParamsInner

class TestResponseInfoAdvertParamsInner(unittest.TestCase):
    """ResponseInfoAdvertParamsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseInfoAdvertParamsInner:
        """Test ResponseInfoAdvertParamsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseInfoAdvertParamsInner`
        """
        model = ResponseInfoAdvertParamsInner()
        if include_optional:
            return ResponseInfoAdvertParamsInner(
                subject_name = '',
                active = True,
                intervals = [
                    wildberries_async_api_client.models.response_info_advert_params_inner_intervals_inner.ResponseInfoAdvert_params_inner_intervals_inner(
                        begin = 56, 
                        end = 56, )
                    ],
                price = 56,
                menu_id = 56,
                subject_id = 56,
                set_id = 56,
                set_name = '',
                menu_name = '',
                nms = [
                    wildberries_async_api_client.models.response_info_advert_params_inner_nms_inner.ResponseInfoAdvert_params_inner_nms_inner(
                        nm = 56, 
                        active = True, )
                    ]
            )
        else:
            return ResponseInfoAdvertParamsInner(
        )
        """

    def testResponseInfoAdvertParamsInner(self):
        """Test ResponseInfoAdvertParamsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()