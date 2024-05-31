# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.adv_v1_item_cpm_change_post_request import AdvV1ItemCpmChangePostRequest

class TestAdvV1ItemCpmChangePostRequest(unittest.TestCase):
    """AdvV1ItemCpmChangePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvV1ItemCpmChangePostRequest:
        """Test AdvV1ItemCpmChangePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvV1ItemCpmChangePostRequest`
        """
        model = AdvV1ItemCpmChangePostRequest()
        if include_optional:
            return AdvV1ItemCpmChangePostRequest(
                advert_id = 56,
                item_id = 56,
                cpm = ''
            )
        else:
            return AdvV1ItemCpmChangePostRequest(
                advert_id = 56,
                item_id = 56,
                cpm = '',
        )
        """

    def testAdvV1ItemCpmChangePostRequest(self):
        """Test AdvV1ItemCpmChangePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
