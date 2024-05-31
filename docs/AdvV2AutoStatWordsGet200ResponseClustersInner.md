# AdvV2AutoStatWordsGet200ResponseClustersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | Кластер — набор похожих ключевых фраз | [optional] 
**count** | **int** | Сколько раз товары показывались по всем фразам из кластера | [optional] 
**keywords** | **List[str]** | Ключевые фразы из кластера, по которым товары показывались хотя бы один раз | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v2_auto_stat_words_get200_response_clusters_inner import AdvV2AutoStatWordsGet200ResponseClustersInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV2AutoStatWordsGet200ResponseClustersInner from a JSON string
adv_v2_auto_stat_words_get200_response_clusters_inner_instance = AdvV2AutoStatWordsGet200ResponseClustersInner.from_json(json)
# print the JSON string representation of the object
print(AdvV2AutoStatWordsGet200ResponseClustersInner.to_json())

# convert the object into a dict
adv_v2_auto_stat_words_get200_response_clusters_inner_dict = adv_v2_auto_stat_words_get200_response_clusters_inner_instance.to_dict()
# create an instance of AdvV2AutoStatWordsGet200ResponseClustersInner from a dict
adv_v2_auto_stat_words_get200_response_clusters_inner_from_dict = AdvV2AutoStatWordsGet200ResponseClustersInner.from_dict(adv_v2_auto_stat_words_get200_response_clusters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


