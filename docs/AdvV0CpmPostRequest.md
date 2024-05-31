# AdvV0CpmPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advert_id** | **int** | Идентификатор кампании, где меняется ставка | 
**type** | **int** | &lt;dl&gt; &lt;dt&gt;кампании, где меняется ставка:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;4&lt;/code&gt; - кампания в каталоге &lt;/dd&gt;  &lt;dd&gt;&lt;code&gt;5&lt;/code&gt; - кампания в карточке товара&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;6&lt;/code&gt; - кампания в поиске&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;7&lt;/code&gt; - кампания в рекомендациях на главной странице&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;8&lt;/code&gt; - автоматическая кампания&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;9&lt;/code&gt; - кампания поиск + каталог &lt;/dd&gt; &lt;/dl&gt;  | 
**cpm** | **int** | Новое значение ставки | 
**param** | **int** | Параметр, для которого будет внесено изменение. Является значением &#x60;subjectId&#x60; (для кампании в поиске и рекомендациях), &#x60;setId&#x60; (для кампании в карточке товара) или &#x60;menuId&#x60; (для кампании в каталоге).  &lt;br&gt; Для автоматической кампании указывать этот параметр не требуется.  | 
**instrument** | **int** | тип кампании для изменения ставки в Поиск + Каталог (4 - каталог, 6 - поиск) | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v0_cpm_post_request import AdvV0CpmPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV0CpmPostRequest from a JSON string
adv_v0_cpm_post_request_instance = AdvV0CpmPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV0CpmPostRequest.to_json())

# convert the object into a dict
adv_v0_cpm_post_request_dict = adv_v0_cpm_post_request_instance.to_dict()
# create an instance of AdvV0CpmPostRequest from a dict
adv_v0_cpm_post_request_from_dict = AdvV0CpmPostRequest.from_dict(adv_v0_cpm_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


