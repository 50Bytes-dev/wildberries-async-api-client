# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.nm_report_get_reports_response_data_inner import NmReportGetReportsResponseDataInner

class TestNmReportGetReportsResponseDataInner(unittest.TestCase):
    """NmReportGetReportsResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NmReportGetReportsResponseDataInner:
        """Test NmReportGetReportsResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NmReportGetReportsResponseDataInner`
        """
        model = NmReportGetReportsResponseDataInner()
        if include_optional:
            return NmReportGetReportsResponseDataInner(
                id = '06eae887-9d9f-491f-b16a-bb1766fcb8d2',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'SUCCESS',
                name = 'Card report',
                size = 123,
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return NmReportGetReportsResponseDataInner(
        )
        """

    def testNmReportGetReportsResponseDataInner(self):
        """Test NmReportGetReportsResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
