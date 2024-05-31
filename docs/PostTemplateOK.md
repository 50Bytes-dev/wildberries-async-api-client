# PostTemplateOK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostTemplateOKData**](PostTemplateOKData.md) |  | [optional] 
**error** | **bool** | Есть ли ошибка | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **List[str]** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.post_template_ok import PostTemplateOK

# TODO update the JSON string below
json = "{}"
# create an instance of PostTemplateOK from a JSON string
post_template_ok_instance = PostTemplateOK.from_json(json)
# print the JSON string representation of the object
print(PostTemplateOK.to_json())

# convert the object into a dict
post_template_ok_dict = post_template_ok_instance.to_dict()
# create an instance of PostTemplateOK from a dict
post_template_ok_from_dict = PostTemplateOK.from_dict(post_template_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


