# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics import NmReportGroupedResponseDataGroupsInnerStatistics

class TestNmReportGroupedResponseDataGroupsInnerStatistics(unittest.TestCase):
    """NmReportGroupedResponseDataGroupsInnerStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NmReportGroupedResponseDataGroupsInnerStatistics:
        """Test NmReportGroupedResponseDataGroupsInnerStatistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NmReportGroupedResponseDataGroupsInnerStatistics`
        """
        model = NmReportGroupedResponseDataGroupsInnerStatistics()
        if include_optional:
            return NmReportGroupedResponseDataGroupsInnerStatistics(
                selected_period = wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_selected_period.NmReportGroupedResponse_data_groups_inner_statistics_selectedPeriod(
                    begin = '{}', 
                    end = '{}', 
                    open_card_count = 0, 
                    add_to_cart_count = 0, 
                    orders_count = 0, 
                    orders_sum_rub = 0, 
                    buyouts_count = 0, 
                    buyouts_sum_rub = 0, 
                    cancel_count = 0, 
                    cancel_sum_rub = 0, 
                    avg_price_rub = 0, 
                    avg_orders_count_per_day = 0, 
                    conversions = wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner_statistics_selected_period_conversions.NmReportDetailResponse_data_cards_inner_statistics_selectedPeriod_conversions(
                        add_to_cart_percent = 0, 
                        cart_to_order_percent = 0, 
                        buyouts_percent = 0, ), ),
                previous_period = wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_previous_period.NmReportGroupedResponse_data_groups_inner_statistics_previousPeriod(
                    begin = '{}', 
                    end = '{}', 
                    open_card_count = 466, 
                    add_to_cart_count = 72, 
                    orders_count = 84, 
                    orders_sum_rub = 127060.42, 
                    buyouts_count = 69, 
                    buyouts_sum_rub = 104898.42, 
                    cancel_count = 13, 
                    cancel_sum_rub = 0, 
                    avg_price_rub = 1562.65, 
                    avg_orders_count_per_day = 0.72, 
                    conversions = wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_previous_period_conversions.NmReportGroupedResponse_data_groups_inner_statistics_previousPeriod_conversions(
                        add_to_cart_percent = 15.5, 
                        cart_to_order_percent = 116.7, 
                        buyouts_percent = 84.1, ), ),
                period_comparison = wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_period_comparison.NmReportGroupedResponse_data_groups_inner_statistics_periodComparison(
                    open_card_dynamics = -100, 
                    add_to_cart_dynamics = -100, 
                    orders_count_dynamics = -100, 
                    orders_sum_rub_dynamics = -100, 
                    buyouts_count_dynamics = -100, 
                    buyouts_sum_rub_dynamics = -100, 
                    cancel_count_dynamics = 0, 
                    cancel_sum_rub_dynamics = 0, 
                    avg_orders_count_per_day_dynamics = 0, 
                    avg_price_rub_dynamics = -100, 
                    conversions = wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_period_comparison_conversions.NmReportGroupedResponse_data_groups_inner_statistics_periodComparison_conversions(
                        add_to_cart_percent = -100, 
                        cart_to_order_percent = -100, 
                        buyouts_percent = -100, ), )
            )
        else:
            return NmReportGroupedResponseDataGroupsInnerStatistics(
        )
        """

    def testNmReportGroupedResponseDataGroupsInnerStatistics(self):
        """Test NmReportGroupedResponseDataGroupsInnerStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()