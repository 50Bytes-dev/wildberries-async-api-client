# ContentV2GetCardsListPost200ResponseCardsInnerTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор тега | [optional] 
**name** | **str** | Название тега | [optional] 
**color** | **str** | Цвет тега. &lt;dl&gt; &lt;dt&gt;Доступные цвета:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;D1CFD7&lt;/code&gt; - серый&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;FEE0E0&lt;/code&gt; - красный&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;ECDAFF&lt;/code&gt; - фиолетовый&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;E4EAFF&lt;/code&gt; - синий&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;DEF1DD&lt;/code&gt; - зеленый&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;FFECC7&lt;/code&gt; - желтый&lt;/dd&gt; &lt;/dl&gt;          | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post200_response_cards_inner_tags_inner import ContentV2GetCardsListPost200ResponseCardsInnerTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPost200ResponseCardsInnerTagsInner from a JSON string
content_v2_get_cards_list_post200_response_cards_inner_tags_inner_instance = ContentV2GetCardsListPost200ResponseCardsInnerTagsInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPost200ResponseCardsInnerTagsInner.to_json())

# convert the object into a dict
content_v2_get_cards_list_post200_response_cards_inner_tags_inner_dict = content_v2_get_cards_list_post200_response_cards_inner_tags_inner_instance.to_dict()
# create an instance of ContentV2GetCardsListPost200ResponseCardsInnerTagsInner from a dict
content_v2_get_cards_list_post200_response_cards_inner_tags_inner_from_dict = ContentV2GetCardsListPost200ResponseCardsInnerTagsInner.from_dict(content_v2_get_cards_list_post200_response_cards_inner_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


