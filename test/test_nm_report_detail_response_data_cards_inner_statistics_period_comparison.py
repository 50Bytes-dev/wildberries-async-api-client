# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner_statistics_period_comparison import NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison

class TestNmReportDetailResponseDataCardsInnerStatisticsPeriodComparison(unittest.TestCase):
    """NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison:
        """Test NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison`
        """
        model = NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison()
        if include_optional:
            return NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison(
                open_card_dynamics = 0,
                add_to_cart_dynamics = 0,
                orders_count_dynamics = -100,
                orders_sum_rub_dynamics = -100,
                buyouts_count_dynamics = -100,
                buyouts_sum_rub_dynamics = -100,
                cancel_count_dynamics = 0,
                cancel_sum_rub_dynamics = 0,
                avg_orders_count_per_day_dynamics = 0,
                avg_price_rub_dynamics = -100,
                conversions = wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner_statistics_period_comparison_conversions.NmReportDetailResponse_data_cards_inner_statistics_periodComparison_conversions(
                    add_to_cart_percent = 0, 
                    cart_to_order_percent = 0, 
                    buyouts_percent = -100, )
            )
        else:
            return NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison(
        )
        """

    def testNmReportDetailResponseDataCardsInnerStatisticsPeriodComparison(self):
        """Test NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()