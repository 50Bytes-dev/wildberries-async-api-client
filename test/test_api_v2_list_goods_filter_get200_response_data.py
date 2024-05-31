# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.api_v2_list_goods_filter_get200_response_data import ApiV2ListGoodsFilterGet200ResponseData

class TestApiV2ListGoodsFilterGet200ResponseData(unittest.TestCase):
    """ApiV2ListGoodsFilterGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2ListGoodsFilterGet200ResponseData:
        """Test ApiV2ListGoodsFilterGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2ListGoodsFilterGet200ResponseData`
        """
        model = ApiV2ListGoodsFilterGet200ResponseData()
        if include_optional:
            return ApiV2ListGoodsFilterGet200ResponseData(
                list_goods = [
                    wildberries_async_api_client.models.goods_list.GoodsList(
                        nm_id = 98486, 
                        vendor_code = '07326060', 
                        sizes = [
                            wildberries_async_api_client.models.goods_list_sizes_inner.GoodsList_sizes_inner(
                                size_id = 3123515574, 
                                price = 500, 
                                discounted_price = 350, 
                                tech_size_name = '42', )
                            ], 
                        currency_iso_code4217 = 'RUB', 
                        discount = 30, 
                        editable_size_price = True, )
                    ]
            )
        else:
            return ApiV2ListGoodsFilterGet200ResponseData(
        )
        """

    def testApiV2ListGoodsFilterGet200ResponseData(self):
        """Test ApiV2ListGoodsFilterGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
