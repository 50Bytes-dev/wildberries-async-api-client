# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.commission_uzbekistan_report_inner import CommissionUzbekistanReportInner

class TestCommissionUzbekistanReportInner(unittest.TestCase):
    """CommissionUzbekistanReportInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommissionUzbekistanReportInner:
        """Test CommissionUzbekistanReportInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommissionUzbekistanReportInner`
        """
        model = CommissionUzbekistanReportInner()
        if include_optional:
            return CommissionUzbekistanReportInner(
                kgvp_uzbekistan = 1.337,
                parent_id = 56,
                parent_name = '',
                subject_id = 56,
                subject_name = ''
            )
        else:
            return CommissionUzbekistanReportInner(
        )
        """

    def testCommissionUzbekistanReportInner(self):
        """Test CommissionUzbekistanReportInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
