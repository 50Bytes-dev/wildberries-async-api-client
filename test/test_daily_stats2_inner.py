# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.daily_stats2_inner import DailyStats2Inner

class TestDailyStats2Inner(unittest.TestCase):
    """DailyStats2Inner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DailyStats2Inner:
        """Test DailyStats2Inner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DailyStats2Inner`
        """
        model = DailyStats2Inner()
        if include_optional:
            return DailyStats2Inner(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                app_type_stats = [
                    wildberries_async_api_client.models.daily_stats2_inner_app_type_stats_inner.DailyStats2_inner_app_type_stats_inner(
                        app_type = 56, 
                        stats = [
                            wildberries_async_api_client.models.stats2_inner.Stats2_inner(
                                views = 56, 
                                clicks = 56, 
                                atbs = 56, 
                                orders = 56, 
                                cr = 1.337, 
                                ctr = 1.337, )
                            ], )
                    ]
            )
        else:
            return DailyStats2Inner(
        )
        """

    def testDailyStats2Inner(self):
        """Test DailyStats2Inner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()