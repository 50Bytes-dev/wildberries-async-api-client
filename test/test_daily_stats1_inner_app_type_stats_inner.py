# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.daily_stats1_inner_app_type_stats_inner import DailyStats1InnerAppTypeStatsInner

class TestDailyStats1InnerAppTypeStatsInner(unittest.TestCase):
    """DailyStats1InnerAppTypeStatsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DailyStats1InnerAppTypeStatsInner:
        """Test DailyStats1InnerAppTypeStatsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DailyStats1InnerAppTypeStatsInner`
        """
        model = DailyStats1InnerAppTypeStatsInner()
        if include_optional:
            return DailyStats1InnerAppTypeStatsInner(
                app_type = 56,
                stats = [
                    wildberries_async_api_client.models.stats1_inner.Stats1_inner(
                        views = 56, 
                        clicks = 56, 
                        atbs = 56, 
                        ctr = 1.337, )
                    ]
            )
        else:
            return DailyStats1InnerAppTypeStatsInner(
        )
        """

    def testDailyStats1InnerAppTypeStatsInner(self):
        """Test DailyStats1InnerAppTypeStatsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
