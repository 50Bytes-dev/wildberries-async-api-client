# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.adv_v1_seacat_stat_get200_response import AdvV1SeacatStatGet200Response

class TestAdvV1SeacatStatGet200Response(unittest.TestCase):
    """AdvV1SeacatStatGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvV1SeacatStatGet200Response:
        """Test AdvV1SeacatStatGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvV1SeacatStatGet200Response`
        """
        model = AdvV1SeacatStatGet200Response()
        if include_optional:
            return AdvV1SeacatStatGet200Response(
                total_views = 56,
                total_clicks = 56,
                total_orders = 56,
                total_sum = 56,
                dates = [
                    wildberries_async_api_client.models._adv_v1_seacat_stat_get_200_response_dates_inner._adv_v1_seacat_stat_get_200_response_dates_inner(
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        search = wildberries_async_api_client.models._adv_v1_seacat_stat_get_200_response_dates_inner_search._adv_v1_seacat_stat_get_200_response_dates_inner_search(
                            views = 56, 
                            clicks = 56, 
                            orders = 56, 
                            sum = 56, ), 
                        catalog = wildberries_async_api_client.models._adv_v1_seacat_stat_get_200_response_dates_inner_catalog._adv_v1_seacat_stat_get_200_response_dates_inner_catalog(
                            views = 56, 
                            clicks = 56, 
                            orders = 56, 
                            sum = 56, ), )
                    ]
            )
        else:
            return AdvV1SeacatStatGet200Response(
        )
        """

    def testAdvV1SeacatStatGet200Response(self):
        """Test AdvV1SeacatStatGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()