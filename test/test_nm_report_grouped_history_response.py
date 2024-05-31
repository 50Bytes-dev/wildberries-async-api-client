# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.nm_report_grouped_history_response import NmReportGroupedHistoryResponse

class TestNmReportGroupedHistoryResponse(unittest.TestCase):
    """NmReportGroupedHistoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NmReportGroupedHistoryResponse:
        """Test NmReportGroupedHistoryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NmReportGroupedHistoryResponse`
        """
        model = NmReportGroupedHistoryResponse()
        if include_optional:
            return NmReportGroupedHistoryResponse(
                data = [
                    wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner.NmReportGroupedHistoryResponse_data_inner(
                        object = wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner_object.NmReportGroupedHistoryResponse_data_inner_object(
                            id = 358, 
                            name = 'Шампуни', ), 
                        brand_name = 'Some', 
                        tag = wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner_tag.NmReportGroupedHistoryResponse_data_inner_tag(
                            id = 123, 
                            name = 'Sale', ), 
                        history = [
                            wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner_history_inner.NmReportGroupedHistoryResponse_data_inner_history_inner(
                                dt = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                open_card_count = 0, 
                                add_to_cart_count = 0, 
                                orders_count = 0, 
                                orders_sum_rub = 0, 
                                buyouts_count = 0, 
                                buyouts_sum_rub = 0, 
                                buyout_percent = 0, 
                                add_to_cart_conversion = 0, 
                                cart_to_order_conversion = 0, )
                            ], )
                    ],
                error = True,
                error_text = '',
                additional_errors = [
                    wildberries_async_api_client.models.response_error_additional_errors_inner.responseError_additionalErrors_inner(
                        field = '', 
                        description = '', )
                    ]
            )
        else:
            return NmReportGroupedHistoryResponse(
        )
        """

    def testNmReportGroupedHistoryResponse(self):
        """Test NmReportGroupedHistoryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
