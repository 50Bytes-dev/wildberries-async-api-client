# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.response_info_advert_type9 import ResponseInfoAdvertType9

class TestResponseInfoAdvertType9(unittest.TestCase):
    """ResponseInfoAdvertType9 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseInfoAdvertType9:
        """Test ResponseInfoAdvertType9
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseInfoAdvertType9`
        """
        model = ResponseInfoAdvertType9()
        if include_optional:
            return ResponseInfoAdvertType9(
                advert_id = 56,
                name = '',
                type = 56,
                status = 56,
                daily_budget = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                change_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                united_params = [
                    wildberries_async_api_client.models.response_info_advert_type9_united_params_inner.ResponseInfoAdvertType9_unitedParams_inner(
                        subject = wildberries_async_api_client.models.response_info_advert_type9_united_params_inner_subject.ResponseInfoAdvertType9_unitedParams_inner_subject(
                            id = 56, 
                            name = '', ), 
                        menus = [
                            wildberries_async_api_client.models.response_info_advert_type9_united_params_inner_menus_inner.ResponseInfoAdvertType9_unitedParams_inner_menus_inner(
                                id = 56, 
                                name = '', )
                            ], 
                        nms = [
                            56
                            ], 
                        search_cpm = 56, 
                        catalog_cpm = 56, )
                    ]
            )
        else:
            return ResponseInfoAdvertType9(
        )
        """

    def testResponseInfoAdvertType9(self):
        """Test ResponseInfoAdvertType9"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
