# wildberries_async_api_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_claim_patch**](DefaultApi.md#api_v1_claim_patch) | **PATCH** /api/v1/claim | Ответ на заявку покупателя
[**api_v1_claims_get**](DefaultApi.md#api_v1_claims_get) | **GET** /api/v1/claims | Заявки покупателей на возврат
[**api_v1_seller_chats_get**](DefaultApi.md#api_v1_seller_chats_get) | **GET** /api/v1/seller/chats | Список чатов
[**api_v1_seller_events_get**](DefaultApi.md#api_v1_seller_events_get) | **GET** /api/v1/seller/events | События чатов
[**api_v1_seller_message_post**](DefaultApi.md#api_v1_seller_message_post) | **POST** /api/v1/seller/message | Отправить сообщение


# **api_v1_claim_patch**
> api_v1_claim_patch(api_v1_claim_patch_request)

Ответ на заявку покупателя

Отправляет ответ на заявку покупателя на возврат.<br> Максимум 20 запросов в минуту 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.api_v1_claim_patch_request import ApiV1ClaimPatchRequest
from wildberries_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wildberries_async_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderApiKey
configuration.api_key['HeaderApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wildberries_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wildberries_async_api_client.DefaultApi(api_client)
    api_v1_claim_patch_request = wildberries_async_api_client.ApiV1ClaimPatchRequest() # ApiV1ClaimPatchRequest | Ответ на заявку

    try:
        # Ответ на заявку покупателя
        await api_instance.api_v1_claim_patch(api_v1_claim_patch_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_claim_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_claim_patch_request** | [**ApiV1ClaimPatchRequest**](ApiV1ClaimPatchRequest.md)| Ответ на заявку | 

### Return type

void (empty response body)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешно |  -  |
**400** | Некорректный запрос |  -  |
**401** | Ошибка авторизации |  -  |
**429** | Слишком много запросов |  -  |
**5XX** | Прочие ошибки |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_claims_get**
> ApiV1ClaimsGet200Response api_v1_claims_get(is_archive, limit, id=id, offset=offset, nm_id=nm_id)

Заявки покупателей на возврат

Возвращает заявки покупателей на возврат товаров за текущие 14 дней.<br> Максимум 20 запросов в минуту 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.api_v1_claims_get200_response import ApiV1ClaimsGet200Response
from wildberries_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wildberries_async_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderApiKey
configuration.api_key['HeaderApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wildberries_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wildberries_async_api_client.DefaultApi(api_client)
    is_archive = true # bool | Состояние заявки:   * `false` — на рассмотрении   * `true` — в архиве 
    limit = 10 # int | Сколько элементов вывести на одной странице (пагинация). Максимум 1 000 элементов
    id = 'fe3e9337-e9f9-423c-8930-946a8ebef80' # str | ID заявки (optional)
    offset = 0 # int | Сколько элементов пропустить (optional)
    nm_id = 196320101 # int | Артикул WB (optional)

    try:
        # Заявки покупателей на возврат
        api_response = await api_instance.api_v1_claims_get(is_archive, limit, id=id, offset=offset, nm_id=nm_id)
        print("The response of DefaultApi->api_v1_claims_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_claims_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive** | **bool**| Состояние заявки:   * &#x60;false&#x60; — на рассмотрении   * &#x60;true&#x60; — в архиве  | 
 **limit** | **int**| Сколько элементов вывести на одной странице (пагинация). Максимум 1 000 элементов | 
 **id** | **str**| ID заявки | [optional] 
 **offset** | **int**| Сколько элементов пропустить | [optional] 
 **nm_id** | **int**| Артикул WB | [optional] 

### Return type

[**ApiV1ClaimsGet200Response**](ApiV1ClaimsGet200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешно |  -  |
**400** | Некорректный запрос |  -  |
**401** | Ошибка авторизации |  -  |
**429** | Слишком много запросов |  -  |
**5XX** | Прочие ошибки |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_seller_chats_get**
> ChatsResponse api_v1_seller_chats_get()

Список чатов

Возвращает список всех чатов продавца.  Максимум 10 запросов за 10 секунд 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.chats_response import ChatsResponse
from wildberries_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wildberries_async_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderApiKey
configuration.api_key['HeaderApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wildberries_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wildberries_async_api_client.DefaultApi(api_client)

    try:
        # Список чатов
        api_response = await api_instance.api_v1_seller_chats_get()
        print("The response of DefaultApi->api_v1_seller_chats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_seller_chats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ChatsResponse**](ChatsResponse.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешно |  -  |
**400** | Некорректный запрос |  -  |
**403** | Доступ запрещён |  -  |
**429** | Слишком много запросов |  -  |
**500** | Внутренняя ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_seller_events_get**
> EventsResponse api_v1_seller_events_get(next=next)

События чатов

Возвращает список событий всех чатов. Чтобы получить все события: <br>1. Сделайте первый запрос без параметра `next`. <br>2. Повторяйте запрос со значением параметра `next` из ответа на предыдущий запрос, пока `totalEvents` не станет равным `0`. Это будет означать, что вы получили все события. <br>Чтобы получать только новые события, укажите параметр `next` со значением поля `addTimestamp` из последнего полученного события. <br> Максимум 10 запросов за 10 секунд 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.events_response import EventsResponse
from wildberries_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wildberries_async_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderApiKey
configuration.api_key['HeaderApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wildberries_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wildberries_async_api_client.DefaultApi(api_client)
    next = 56 # int | Пагинатор. С какого момента получить следующий пакет данных.<br>Формат Unix timestamp **с миллисекундами**  (optional)

    try:
        # События чатов
        api_response = await api_instance.api_v1_seller_events_get(next=next)
        print("The response of DefaultApi->api_v1_seller_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_seller_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next** | **int**| Пагинатор. С какого момента получить следующий пакет данных.&lt;br&gt;Формат Unix timestamp **с миллисекундами**  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешно |  -  |
**400** | Некорректный запрос |  -  |
**403** | Доступ запрещён |  -  |
**429** | Слишком много запросов |  -  |
**500** | Внутренняя ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_seller_message_post**
> MessageResponse api_v1_seller_message_post(reply_sign, message=message, file=file)

Отправить сообщение

Отправляет сообщения покупателю. Максимум 10 запросов за 10 секунд 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.message_response import MessageResponse
from wildberries_async_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wildberries_async_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderApiKey
configuration.api_key['HeaderApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wildberries_async_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wildberries_async_api_client.DefaultApi(api_client)
    reply_sign = 'reply_sign_example' # str | Подпись чата. Можно получить из [информации по чату](./#/paths/~1api~1v1~1seller~1chats/get) или [данных события](./#/paths/~1api~1v1~1seller~1events/get), если в событии есть поле `\\\"isNewChat\\\": true`. 
    message = 'message_example' # str | Текст сообщения. Максимум 1000 символов. (optional)
    file = None # List[bytearray] | Файлы, формат JPEG, PDF или PNG, максимальный размер — 5 Мб каждый. Максимальный суммарный размер файлов — 30 Мб.  (optional)

    try:
        # Отправить сообщение
        api_response = await api_instance.api_v1_seller_message_post(reply_sign, message=message, file=file)
        print("The response of DefaultApi->api_v1_seller_message_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_seller_message_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_sign** | **str**| Подпись чата. Можно получить из [информации по чату](./#/paths/~1api~1v1~1seller~1chats/get) или [данных события](./#/paths/~1api~1v1~1seller~1events/get), если в событии есть поле &#x60;\\\&quot;isNewChat\\\&quot;: true&#x60;.  | 
 **message** | **str**| Текст сообщения. Максимум 1000 символов. | [optional] 
 **file** | **List[bytearray]**| Файлы, формат JPEG, PDF или PNG, максимальный размер — 5 Мб каждый. Максимальный суммарный размер файлов — 30 Мб.  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешно |  -  |
**400** | Некорректный запрос |  -  |
**403** | Доступ запрещён |  -  |
**429** | Слишком много запросов |  -  |
**500** | Внутренняя ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

