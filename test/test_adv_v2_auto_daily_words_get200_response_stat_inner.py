# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.adv_v2_auto_daily_words_get200_response_stat_inner import AdvV2AutoDailyWordsGet200ResponseStatInner

class TestAdvV2AutoDailyWordsGet200ResponseStatInner(unittest.TestCase):
    """AdvV2AutoDailyWordsGet200ResponseStatInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvV2AutoDailyWordsGet200ResponseStatInner:
        """Test AdvV2AutoDailyWordsGet200ResponseStatInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvV2AutoDailyWordsGet200ResponseStatInner`
        """
        model = AdvV2AutoDailyWordsGet200ResponseStatInner()
        if include_optional:
            return AdvV2AutoDailyWordsGet200ResponseStatInner(
                keyword = 'Смартфон',
                views = 100,
                clicks = 500,
                ctr = 0.5,
                sum = 1000
            )
        else:
            return AdvV2AutoDailyWordsGet200ResponseStatInner(
        )
        """

    def testAdvV2AutoDailyWordsGet200ResponseStatInner(self):
        """Test AdvV2AutoDailyWordsGet200ResponseStatInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
