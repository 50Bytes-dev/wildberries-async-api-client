# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.response_info_advert_type8_auto_params_nm_cpm_inner import ResponseInfoAdvertType8AutoParamsNmCPMInner

class TestResponseInfoAdvertType8AutoParamsNmCPMInner(unittest.TestCase):
    """ResponseInfoAdvertType8AutoParamsNmCPMInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseInfoAdvertType8AutoParamsNmCPMInner:
        """Test ResponseInfoAdvertType8AutoParamsNmCPMInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseInfoAdvertType8AutoParamsNmCPMInner`
        """
        model = ResponseInfoAdvertType8AutoParamsNmCPMInner()
        if include_optional:
            return ResponseInfoAdvertType8AutoParamsNmCPMInner(
                nm = 56,
                cpm = 56
            )
        else:
            return ResponseInfoAdvertType8AutoParamsNmCPMInner(
        )
        """

    def testResponseInfoAdvertType8AutoParamsNmCPMInner(self):
        """Test ResponseInfoAdvertType8AutoParamsNmCPMInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
