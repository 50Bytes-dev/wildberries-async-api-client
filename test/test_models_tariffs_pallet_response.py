# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.models_tariffs_pallet_response import ModelsTariffsPalletResponse

class TestModelsTariffsPalletResponse(unittest.TestCase):
    """ModelsTariffsPalletResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelsTariffsPalletResponse:
        """Test ModelsTariffsPalletResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelsTariffsPalletResponse`
        """
        model = ModelsTariffsPalletResponse()
        if include_optional:
            return ModelsTariffsPalletResponse(
                data = wildberries_async_api_client.models.models/warehouses_pallet_rates.models.WarehousesPalletRates(
                    dt_from_min = '{}', 
                    dt_next_pallet = '{}', 
                    dt_till_max = '{}', 
                    warehouse_list = [
                        wildberries_async_api_client.models.models/warehouse_pallet_rates.models.WarehousePalletRates(
                            pallet_delivery_expr = '20', 
                            pallet_delivery_value_base = '150', 
                            pallet_delivery_value_liter = '50', 
                            pallet_storage_expr = '20', 
                            pallet_storage_value_expr = '200', 
                            warehouse_name = 'Коледино', )
                        ], )
            )
        else:
            return ModelsTariffsPalletResponse(
        )
        """

    def testModelsTariffsPalletResponse(self):
        """Test ModelsTariffsPalletResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
