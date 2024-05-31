# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v1_analytics_storage_coefficient_get200_response_report_inner import ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner

class TestApiV1AnalyticsStorageCoefficientGet200ResponseReportInner(unittest.TestCase):
    """ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner:
        """Test ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner`
        """
        model = ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner()
        if include_optional:
            return ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner(
                actual_height = 6,
                actual_length = 39,
                actual_volume = 7.02,
                actual_width = 30,
                var_date = '{}',
                dimension_difference = 101.74,
                height = 10,
                length = 30,
                log_warehouse_coef = 1,
                nm_id = 123456789,
                photo_urls = '["https://photos.wbstatic.net/handheld-goods-measurements-photo/123456789_73984211-e6c3-44e2-66af-0d44d2620308.jpg","https://photos.wbstatic.net/handheld-goods-measurements-photo/123456789_8ee5ff5e-c6bb-426c-7d12-c2dd228c0f62.jpg"]',
                title = 'Сухой корм для крупных собак ассорти мясное, 10 кг',
                volume = 6.9,
                width = 23
            )
        else:
            return ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner(
        )
        """

    def testApiV1AnalyticsStorageCoefficientGet200ResponseReportInner(self):
        """Test ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()