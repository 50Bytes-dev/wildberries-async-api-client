# ContentV2CardsErrorListGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Категория для который создавалось КТ с данной НМ | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**update_at** | **str** | Дата и время запроса на создание КТ с данным НМ | [optional] 
**errors** | **List[str]** | Список ошибок из-за которых не обработался запрос на создание КТ с данным НМ | [optional] 
**object_id** | **int** | Идентификатор предмета | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_error_list_get200_response_data_inner import ContentV2CardsErrorListGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsErrorListGet200ResponseDataInner from a JSON string
content_v2_cards_error_list_get200_response_data_inner_instance = ContentV2CardsErrorListGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsErrorListGet200ResponseDataInner.to_json())

# convert the object into a dict
content_v2_cards_error_list_get200_response_data_inner_dict = content_v2_cards_error_list_get200_response_data_inner_instance.to_dict()
# create an instance of ContentV2CardsErrorListGet200ResponseDataInner from a dict
content_v2_cards_error_list_get200_response_data_inner_from_dict = ContentV2CardsErrorListGet200ResponseDataInner.from_dict(content_v2_cards_error_list_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


