# ApiV1ClaimsGet200ResponseClaimsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID заявки | [optional] 
**claim_type** | **int** | Источник заявки:   * &#x60;1&#x60; — портал покупателей   * &#x60;3&#x60; — чат  | [optional] 
**status** | **int** | Решение по возврату покупателю:   * &#x60;0&#x60; — на рассмотрении   * &#x60;1&#x60; — отказ   * &#x60;2&#x60; — одобрено  | [optional] 
**status_ex** | **int** | Статус товара:   * &#x60;0&#x60; — на рассмотрении   * &#x60;1&#x60; — остаётся у покупателя   * &#x60;2&#x60; — без возврата                             * &#x60;5&#x60; — без возврата   * &#x60;8&#x60; — товар будет возвращён в реализацию или оформлен на возврат после проверки WB   * &#x60;10&#x60; — возврат продавцу  | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**user_comment** | **str** | Комментарий покупателя | [optional] 
**wb_comment** | **str** | Ответ покупателю | [optional] 
**dt** | **datetime** | Дата и время оформления заявки покупателем | [optional] 
**imt_name** | **str** | Название товара | [optional] 
**order_dt** | **datetime** | Дата и время заказа | [optional] 
**dt_update** | **datetime** | Дата и время рассмотрения заявки. Для нерассмотренной заявки — дата и время оформления | [optional] 
**photos** | **List[str]** | Фотографии из заявки покупателя | [optional] 
**video_paths** | **List[str]** | Видео из заявки покупателя | [optional] 
**actions** | **List[str]** | Варианты ответа продавца.&lt;br&gt; Отклонённые заявки можно пересмотреть. Если массив пуст, с заявкой работать нельзя.   * &#x60;approve1&#x60; — одобрить с проверкой брака.&lt;br&gt;Деньги вернутся покупателю после возврата товара. Товар будет проверен на складе. При подтверждении брака/ошибки вложения товар будет отправлен продавцу. Если брак/ошибка вложения не подтвердятся, товар будет возвращён в продажу.   * &#x60;approve2&#x60; — одобрить и забрать товар.&lt;br&gt; Деньги вернутся покупателю после возврата товара. Товар будет отправлен продавцу.   * &#x60;autorefund1&#x60; — одобрить без возврата товара.&lt;br&gt; Товар останется у покупателя. Деньги за него будут возвращены покупателю без возврата товара.   * &#x60;reject1&#x60; — отклонить с шаблоном ответа: &lt;details&gt;&lt;summary&gt;&lt;strong&gt;Брак не обнаружен&lt;/strong&gt;&lt;/summary&gt;Здравствуйте! Заявка онлайн на проверку качества товара рассмотрена.&lt;br&gt;По предоставленной информации (фото, видео, комментарий) брак не подтвержден.&lt;/details&gt;   * &#x60;reject2&#x60; — отклонить с шаблоном ответа: &lt;details&gt;&lt;summary&gt;&lt;strong&gt;Добавить фото/видео&lt;/strong&gt;&lt;/summary&gt;Добрый день! Заявка онлайн на проверку качества товара рассмотрена и отклонена по причине некорректного оформления. Обращаем Ваше внимание, что в комментариях должна быть представлена информация (описание) о наличии предполагаемого производственного брака, а фотографии (не менее двух) и (или) видео - отображать следующую информацию:&lt;br&gt;1. Обзорное изображение товара целиком&lt;br&gt;2. Крупный план вшивной бирки (или другая маркировка товара)&lt;br&gt;3. При наличии упаковки со штрих-кодом - фото ШК.&lt;br&gt;4. Предполагаемый дефект товара.&lt;br&gt;Просим Вас переоформить заявку с соблюдением необходимых условий.&lt;/details&gt;   * &#x60;reject3&#x60; — отклонить с шаблоном ответа: &lt;details&gt;&lt;summary&gt;&lt;strong&gt;Направить в сервисный центр&lt;/strong&gt;&lt;/summary&gt;Здравствуйте! Мы внимательно прочитали заявку, проверили фото и видео. К сожалению, мы не нашли брак, повреждение или несоответствие описанию в вашем товаре. Обратитесь напрямую в сервисный центр — его адрес и контакты есть на сайте производителя или на гарантийном талоне. Там проведут окончательную проверку товара и выдадут вам акт. Если центр нашёл брак, то отправьте этот акт в чат на нашем сайте.&lt;/details&gt;  | [optional] 
**price** | **float** | Фактическая цена с учетом всех скидок. Взимается с покупателя | [optional] 
**currency_code** | **str** | Код валюты цены | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_claims_get200_response_claims_inner import ApiV1ClaimsGet200ResponseClaimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ClaimsGet200ResponseClaimsInner from a JSON string
api_v1_claims_get200_response_claims_inner_instance = ApiV1ClaimsGet200ResponseClaimsInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1ClaimsGet200ResponseClaimsInner.to_json())

# convert the object into a dict
api_v1_claims_get200_response_claims_inner_dict = api_v1_claims_get200_response_claims_inner_instance.to_dict()
# create an instance of ApiV1ClaimsGet200ResponseClaimsInner from a dict
api_v1_claims_get200_response_claims_inner_from_dict = ApiV1ClaimsGet200ResponseClaimsInner.from_dict(api_v1_claims_get200_response_claims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


