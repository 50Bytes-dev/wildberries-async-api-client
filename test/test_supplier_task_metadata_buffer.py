# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.supplier_task_metadata_buffer import SupplierTaskMetadataBuffer

class TestSupplierTaskMetadataBuffer(unittest.TestCase):
    """SupplierTaskMetadataBuffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupplierTaskMetadataBuffer:
        """Test SupplierTaskMetadataBuffer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupplierTaskMetadataBuffer`
        """
        model = SupplierTaskMetadataBuffer()
        if include_optional:
            return SupplierTaskMetadataBuffer(
                upload_id = 395643565,
                status = 1,
                upload_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                activation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                over_all_goods_number = 100,
                success_goods_number = 0
            )
        else:
            return SupplierTaskMetadataBuffer(
        )
        """

    def testSupplierTaskMetadataBuffer(self):
        """Test SupplierTaskMetadataBuffer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
