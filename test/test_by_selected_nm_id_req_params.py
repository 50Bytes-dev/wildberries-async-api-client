# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.by_selected_nm_id_req_params import BySelectedNmIDReqParams

class TestBySelectedNmIDReqParams(unittest.TestCase):
    """BySelectedNmIDReqParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BySelectedNmIDReqParams:
        """Test BySelectedNmIDReqParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BySelectedNmIDReqParams`
        """
        model = BySelectedNmIDReqParams()
        if include_optional:
            return BySelectedNmIDReqParams(
                nm_ids = [
                    56
                    ],
                subject_ids = [
                    56
                    ],
                brand_names = [
                    ''
                    ],
                tag_ids = [
                    56
                    ],
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                timezone = '',
                aggregation_level = 'day',
                skip_deleted_nm = True
            )
        else:
            return BySelectedNmIDReqParams(
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testBySelectedNmIDReqParams(self):
        """Test BySelectedNmIDReqParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
