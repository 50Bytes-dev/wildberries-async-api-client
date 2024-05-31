# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.adv_v1_upd_get200_response_inner import AdvV1UpdGet200ResponseInner

class TestAdvV1UpdGet200ResponseInner(unittest.TestCase):
    """AdvV1UpdGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvV1UpdGet200ResponseInner:
        """Test AdvV1UpdGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvV1UpdGet200ResponseInner`
        """
        model = AdvV1UpdGet200ResponseInner()
        if include_optional:
            return AdvV1UpdGet200ResponseInner(
                upd_num = 56,
                upd_time = '',
                upd_sum = 56,
                advert_id = 56,
                camp_name = '',
                advert_type = 56,
                payment_type = '',
                advert_status = 56
            )
        else:
            return AdvV1UpdGet200ResponseInner(
        )
        """

    def testAdvV1UpdGet200ResponseInner(self):
        """Test AdvV1UpdGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()