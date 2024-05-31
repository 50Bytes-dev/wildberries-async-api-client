# wb_client.Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_files_orders_external_stickers_post**](Api.md#api_v3_files_orders_external_stickers_post) | **POST** /api/v3/files/orders/external-stickers | Получить список ссылок на этикетки для сборочных заданий, которые требуются при кроссбордере
[**api_v3_orders_get**](Api.md#api_v3_orders_get) | **GET** /api/v3/orders | Получить информацию по сборочным заданиям
[**api_v3_orders_new_get**](Api.md#api_v3_orders_new_get) | **GET** /api/v3/orders/new | Получить список новых сборочных заданий
[**api_v3_orders_order_id_cancel_patch**](Api.md#api_v3_orders_order_id_cancel_patch) | **PATCH** /api/v3/orders/{orderId}/cancel | Отменить сборочное задание
[**api_v3_orders_order_id_meta_delete**](Api.md#api_v3_orders_order_id_meta_delete) | **DELETE** /api/v3/orders/{orderId}/meta | Удалить метаданные сборочного задания
[**api_v3_orders_order_id_meta_get**](Api.md#api_v3_orders_order_id_meta_get) | **GET** /api/v3/orders/{orderId}/meta | Получить метаданные сборочного задания
[**api_v3_orders_order_id_meta_gtin_put**](Api.md#api_v3_orders_order_id_meta_gtin_put) | **PUT** /api/v3/orders/{orderId}/meta/gtin | Закрепить за сборочным заданием GTIN
[**api_v3_orders_order_id_meta_imei_put**](Api.md#api_v3_orders_order_id_meta_imei_put) | **PUT** /api/v3/orders/{orderId}/meta/imei | Закрепить за сборочным заданием IMEI
[**api_v3_orders_order_id_meta_sgtin_put**](Api.md#api_v3_orders_order_id_meta_sgtin_put) | **PUT** /api/v3/orders/{orderId}/meta/sgtin | Закрепить за сборочным заданием КиЗ (маркировку Честного знака)
[**api_v3_orders_order_id_meta_uin_put**](Api.md#api_v3_orders_order_id_meta_uin_put) | **PUT** /api/v3/orders/{orderId}/meta/uin | Закрепить за сборочным заданием УИН (уникальный идентификационный номер)
[**api_v3_orders_status_post**](Api.md#api_v3_orders_status_post) | **POST** /api/v3/orders/status | Получить статусы сборочных заданий
[**api_v3_orders_stickers_post**](Api.md#api_v3_orders_stickers_post) | **POST** /api/v3/orders/stickers | Получить этикетки для сборочных заданий
[**api_v3_supplies_orders_reshipment_get**](Api.md#api_v3_supplies_orders_reshipment_get) | **GET** /api/v3/supplies/orders/reshipment | Получить все сборочные задания на повторную отгрузку


# **api_v3_files_orders_external_stickers_post**
> ApiV3FilesOrdersExternalStickersPost200Response api_v3_files_orders_external_stickers_post(api_v3_orders_stickers_post_request=api_v3_orders_stickers_post_request)

Получить список ссылок на этикетки для сборочных заданий, которые требуются при кроссбордере

Возвращает список ссылок на этикетки для сборочных заданий, которые требуются при кроссбордере.  **Ограничения при работе с методом**: - Нельзя запросить больше 100 этикеток за раз (не более 100 идентификаторов сборочных заданий в запросе). - Метод возвращает этикетки только для сборочных заданий, находящихся в доставке (в статусе **complete**). 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_files_orders_external_stickers_post200_response import ApiV3FilesOrdersExternalStickersPost200Response
from wb_client.models.api_v3_orders_stickers_post_request import ApiV3OrdersStickersPostRequest
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    api_v3_orders_stickers_post_request = wb_client.ApiV3OrdersStickersPostRequest() # ApiV3OrdersStickersPostRequest |  (optional)

    try:
        # Получить список ссылок на этикетки для сборочных заданий, которые требуются при кроссбордере
        api_response = await api_instance.api_v3_files_orders_external_stickers_post(api_v3_orders_stickers_post_request=api_v3_orders_stickers_post_request)
        print("The response of Api->api_v3_files_orders_external_stickers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->api_v3_files_orders_external_stickers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v3_orders_stickers_post_request** | [**ApiV3OrdersStickersPostRequest**](ApiV3OrdersStickersPostRequest.md)|  | [optional] 

### Return type

[**ApiV3FilesOrdersExternalStickersPost200Response**](ApiV3FilesOrdersExternalStickersPost200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список ссылок на этикетки |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_get**
> ApiV3OrdersGet200Response api_v3_orders_get(limit, next, date_from=date_from, date_to=date_to)

Получить информацию по сборочным заданиям

Возвращает информацию по сборочным заданиям без их актуального статуса. <br> Данные по сборочному заданию, возвращающиеся в данном методе, не меняются. <br> Рекомендуется использовать для получения исторических данных. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_get200_response import ApiV3OrdersGet200Response
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    limit = 56 # int | Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
    next = 56 # int | Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных. Для получения полного списка данных должен быть равен 0 в первом запросе. Для следующих запросов необходимо брать значения из одноимённого поля в ответе.
    date_from = 56 # int | Дата начала периода в формате Unix timestamp. Необязательный параметр. (optional)
    date_to = 56 # int | Дата конца периода в формате Unix timestamp. Необязательный параметр. (optional)

    try:
        # Получить информацию по сборочным заданиям
        api_response = await api_instance.api_v3_orders_get(limit, next, date_from=date_from, date_to=date_to)
        print("The response of Api->api_v3_orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Параметр пагинации. Устанавливает предельное количество возвращаемых данных. | 
 **next** | **int**| Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных. Для получения полного списка данных должен быть равен 0 в первом запросе. Для следующих запросов необходимо брать значения из одноимённого поля в ответе. | 
 **date_from** | **int**| Дата начала периода в формате Unix timestamp. Необязательный параметр. | [optional] 
 **date_to** | **int**| Дата конца периода в формате Unix timestamp. Необязательный параметр. | [optional] 

### Return type

[**ApiV3OrdersGet200Response**](ApiV3OrdersGet200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список сборочных заданий |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_new_get**
> ApiV3OrdersNewGet200Response api_v3_orders_new_get()

Получить список новых сборочных заданий

Возвращает список всех новых сборочных заданий у продавца на данный момент. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_new_get200_response import ApiV3OrdersNewGet200Response
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)

    try:
        # Получить список новых сборочных заданий
        api_response = await api_instance.api_v3_orders_new_get()
        print("The response of Api->api_v3_orders_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_new_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV3OrdersNewGet200Response**](ApiV3OrdersNewGet200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список сборочных заданий |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_order_id_cancel_patch**
> api_v3_orders_order_id_cancel_patch(order_id)

Отменить сборочное задание

Переводит сборочное задание в статус **cancel** (\"Отменено продавцом\").

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    order_id = 5632423 # int | ID сборочного задания

    try:
        # Отменить сборочное задание
        await api_instance.api_v3_orders_order_id_cancel_patch(order_id)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_order_id_cancel_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID сборочного задания | 

### Return type

void (empty response body)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Отменено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | Ошибка обновления статуса |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_order_id_meta_delete**
> api_v3_orders_order_id_meta_delete(order_id, key=key)

Удалить метаданные сборочного задания

Удаляет значение метаданных заказа для переданного ключа.  <br> Возможные метаданные: <br> **imei** <br> **uin** <br> **gtin** <br> **sgtin** <span class=\"newM\">new</span><br> Передается только одно значение.  

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    order_id = 5632423 # int | ID сборочного задания
    key = 'key_example' # str | Название метаданных для удаления (**imei**, **uin**, **gtin**, **sgtin**). Передается только одно значение. (optional)

    try:
        # Удалить метаданные сборочного задания
        await api_instance.api_v3_orders_order_id_meta_delete(order_id, key=key)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_order_id_meta_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID сборочного задания | 
 **key** | **str**| Название метаданных для удаления (**imei**, **uin**, **gtin**, **sgtin**). Передается только одно значение. | [optional] 

### Return type

void (empty response body)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Удалено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**409** | Ошибка удаления метаданных |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_order_id_meta_get**
> ApiV3OrdersOrderIdMetaGet200Response api_v3_orders_order_id_meta_get(order_id)

Получить метаданные сборочного задания

Возвращает метаданные заказа. <br> Возможные метаданные: <br> **imei** <br> **uin** <br> **gtin** <br> **sgtin**   <br> В ответе метода возвращаются метаданные, доступные для сборочного задания. Если ответ вернулся с пустой структурой **meta**, значит у сборочного задания нет метаданных, и добавление их не доступно.   

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_order_id_meta_get200_response import ApiV3OrdersOrderIdMetaGet200Response
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    order_id = 5632423 # int | ID сборочного задания

    try:
        # Получить метаданные сборочного задания
        api_response = await api_instance.api_v3_orders_order_id_meta_get(order_id)
        print("The response of Api->api_v3_orders_order_id_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_order_id_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID сборочного задания | 

### Return type

[**ApiV3OrdersOrderIdMetaGet200Response**](ApiV3OrdersOrderIdMetaGet200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Метаданные заказа |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_order_id_meta_gtin_put**
> api_v3_orders_order_id_meta_gtin_put(order_id, api_v3_orders_order_id_meta_gtin_put_request=api_v3_orders_order_id_meta_gtin_put_request)

Закрепить за сборочным заданием GTIN

Обновляет GTIN сборочного задания. У одного сборочного задания может быть только один GTIN. Добавлять маркировку можно только для заказов в статусе `confirm` и доставка которых осуществляется силами Wildberries.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_order_id_meta_gtin_put_request import ApiV3OrdersOrderIdMetaGtinPutRequest
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    order_id = 5632423 # int | ID сборочного задания
    api_v3_orders_order_id_meta_gtin_put_request = wb_client.ApiV3OrdersOrderIdMetaGtinPutRequest() # ApiV3OrdersOrderIdMetaGtinPutRequest |  (optional)

    try:
        # Закрепить за сборочным заданием GTIN
        await api_instance.api_v3_orders_order_id_meta_gtin_put(order_id, api_v3_orders_order_id_meta_gtin_put_request=api_v3_orders_order_id_meta_gtin_put_request)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_order_id_meta_gtin_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID сборочного задания | 
 **api_v3_orders_order_id_meta_gtin_put_request** | [**ApiV3OrdersOrderIdMetaGtinPutRequest**](ApiV3OrdersOrderIdMetaGtinPutRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Обновлено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**409** | Ошибка обновления метаданных. |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_order_id_meta_imei_put**
> api_v3_orders_order_id_meta_imei_put(order_id, api_v3_orders_order_id_meta_imei_put_request=api_v3_orders_order_id_meta_imei_put_request)

Закрепить за сборочным заданием IMEI

Обновляет IMEI сборочного задания. У одного сборочного задания может быть только один IMEI. Добавлять маркировку можно только для заказов в статусе `confirm` и доставка которых осуществляется силами Wildberries.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_order_id_meta_imei_put_request import ApiV3OrdersOrderIdMetaImeiPutRequest
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    order_id = 5632423 # int | ID сборочного задания
    api_v3_orders_order_id_meta_imei_put_request = wb_client.ApiV3OrdersOrderIdMetaImeiPutRequest() # ApiV3OrdersOrderIdMetaImeiPutRequest |  (optional)

    try:
        # Закрепить за сборочным заданием IMEI
        await api_instance.api_v3_orders_order_id_meta_imei_put(order_id, api_v3_orders_order_id_meta_imei_put_request=api_v3_orders_order_id_meta_imei_put_request)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_order_id_meta_imei_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID сборочного задания | 
 **api_v3_orders_order_id_meta_imei_put_request** | [**ApiV3OrdersOrderIdMetaImeiPutRequest**](ApiV3OrdersOrderIdMetaImeiPutRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Обновлено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**409** | Ошибка обновления метаданных. |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_order_id_meta_sgtin_put**
> api_v3_orders_order_id_meta_sgtin_put(order_id, api_v3_orders_order_id_meta_sgtin_put_request=api_v3_orders_order_id_meta_sgtin_put_request)

Закрепить за сборочным заданием КиЗ (маркировку Честного знака)

Метод позволяет закрепить за сборочным заданием КиЗ (маркировку Честного знака). <span class=\"newM\">new</span> <br>  Закрепление КиЗ за сборочным заданием возможно только в случае, если это поле возвращается в ответе метода **Получить метаданные сборочного задания**, а сборочное задание находится в статусе `confirm`. <br> <br> Получить загруженные КиЗ можно методом <b>Получить метаданные сборочного задания</b> <br> С правилами работы с КиЗ можно ознакомиться тут: https://честныйзнак.рф <br> <br> 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_order_id_meta_sgtin_put_request import ApiV3OrdersOrderIdMetaSgtinPutRequest
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    order_id = 5632423 # int | ID сборочного задания
    api_v3_orders_order_id_meta_sgtin_put_request = wb_client.ApiV3OrdersOrderIdMetaSgtinPutRequest() # ApiV3OrdersOrderIdMetaSgtinPutRequest |  (optional)

    try:
        # Закрепить за сборочным заданием КиЗ (маркировку Честного знака)
        await api_instance.api_v3_orders_order_id_meta_sgtin_put(order_id, api_v3_orders_order_id_meta_sgtin_put_request=api_v3_orders_order_id_meta_sgtin_put_request)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_order_id_meta_sgtin_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID сборочного задания | 
 **api_v3_orders_order_id_meta_sgtin_put_request** | [**ApiV3OrdersOrderIdMetaSgtinPutRequest**](ApiV3OrdersOrderIdMetaSgtinPutRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Отправлено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | Ошибка добавления маркировки. |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_order_id_meta_uin_put**
> api_v3_orders_order_id_meta_uin_put(order_id, api_v3_orders_order_id_meta_uin_put_request=api_v3_orders_order_id_meta_uin_put_request)

Закрепить за сборочным заданием УИН (уникальный идентификационный номер)

Обновляет УИН сборочного задания. У одного сборочного задания может быть только один УИН. Добавлять маркировку можно только для заказов в статусе `confirm` и доставка которых осуществляется силами Wildberries.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_order_id_meta_uin_put_request import ApiV3OrdersOrderIdMetaUinPutRequest
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    order_id = 5632423 # int | ID сборочного задания
    api_v3_orders_order_id_meta_uin_put_request = wb_client.ApiV3OrdersOrderIdMetaUinPutRequest() # ApiV3OrdersOrderIdMetaUinPutRequest |  (optional)

    try:
        # Закрепить за сборочным заданием УИН (уникальный идентификационный номер)
        await api_instance.api_v3_orders_order_id_meta_uin_put(order_id, api_v3_orders_order_id_meta_uin_put_request=api_v3_orders_order_id_meta_uin_put_request)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_order_id_meta_uin_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| ID сборочного задания | 
 **api_v3_orders_order_id_meta_uin_put_request** | [**ApiV3OrdersOrderIdMetaUinPutRequest**](ApiV3OrdersOrderIdMetaUinPutRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Обновлено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**409** | Ошибка обновления метаданных. |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_status_post**
> ApiV3OrdersStatusPost200Response api_v3_orders_status_post(api_v3_orders_status_post_request=api_v3_orders_status_post_request)

Получить статусы сборочных заданий

Возвращает статусы сборочных заданий по переданному списку идентификаторов сборочных заданий.  **supplierStatus** - статус сборочного задания, триггером изменения которого является сам продавец.<br> Возможны следующие значения данного поля: | Статус   | Описание            | Как перевести сборочное задание в данный статус | | -------  | ---------           | --------------------------------------| | new      | Новое сборочное задание |           | confirm  | На сборке            | При добавлении сборочного задания к поставке **PATCH** */api/v3/supplies/{supplyId}/orders/{orderId}* | complete | В доставке           | При переводе в доставку соответствующей поставки **PATCH** */api/v3/supplies/{supplyId}/deliver* | cancel   | Отменено продавцом   | **PATCH** */api/v3/orders/{orderId}/cancel*   **wbStatus** - статус сборочного задания в системе Wildberries.<br> Возможны следующие значения данного поля: - **waiting** - сборочное задание в работе - **sorted** - сборочное задание отсортировано - **sold** - сборочное задание получено покупателем - **canceled** - отмена сборочного задания - **canceled_by_client** - покупатель отменил заказ при получении - **declined_by_client** - покупатель отменил заказ в первый чаc <span class=\"newM\">new</span> <br> Отмена доступна покупателю в первый час с момента заказа, если заказ не переведён на сборку - **defect** - отмена сборочного задания по причине брака - **ready_for_pickup** - сборочное задание прибыло на ПВЗ 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_status_post200_response import ApiV3OrdersStatusPost200Response
from wb_client.models.api_v3_orders_status_post_request import ApiV3OrdersStatusPostRequest
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    api_v3_orders_status_post_request = wb_client.ApiV3OrdersStatusPostRequest() # ApiV3OrdersStatusPostRequest |  (optional)

    try:
        # Получить статусы сборочных заданий
        api_response = await api_instance.api_v3_orders_status_post(api_v3_orders_status_post_request=api_v3_orders_status_post_request)
        print("The response of Api->api_v3_orders_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v3_orders_status_post_request** | [**ApiV3OrdersStatusPostRequest**](ApiV3OrdersStatusPostRequest.md)|  | [optional] 

### Return type

[**ApiV3OrdersStatusPost200Response**](ApiV3OrdersStatusPost200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список статусов сборочных заданий |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_orders_stickers_post**
> ApiV3OrdersStickersPost200Response api_v3_orders_stickers_post(type, width, height, api_v3_orders_stickers_post_request=api_v3_orders_stickers_post_request)

Получить этикетки для сборочных заданий

Возвращает список этикеток по переданному массиву сборочных заданий. Можно запросить этикетку в формате svg, zplv (вертикальный), zplh (горизонтальный), png.  **Ограничения при работе с методом**: - Нельзя запросить больше 100 этикеток за раз (не более 100 идентификаторов сборочных заданий в запросе). - Метод возвращает этикетки только для сборочных заданий, находящихся на сборке (в статусе **confirm**). - Доступные размеры: <dd>580x400 пикселей, при параметрах width = 58, height = 40</dd> <dd>400x300 пикселей, при параметрах width = 40, height = 30</dd> 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_orders_stickers_post200_response import ApiV3OrdersStickersPost200Response
from wb_client.models.api_v3_orders_stickers_post_request import ApiV3OrdersStickersPostRequest
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)
    type = 'type_example' # str | Тип этикетки
    width = 56 # int | Ширина этикетки
    height = 56 # int | Высота этикетки
    api_v3_orders_stickers_post_request = wb_client.ApiV3OrdersStickersPostRequest() # ApiV3OrdersStickersPostRequest |  (optional)

    try:
        # Получить этикетки для сборочных заданий
        api_response = await api_instance.api_v3_orders_stickers_post(type, width, height, api_v3_orders_stickers_post_request=api_v3_orders_stickers_post_request)
        print("The response of Api->api_v3_orders_stickers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->api_v3_orders_stickers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Тип этикетки | 
 **width** | **int**| Ширина этикетки | 
 **height** | **int**| Высота этикетки | 
 **api_v3_orders_stickers_post_request** | [**ApiV3OrdersStickersPostRequest**](ApiV3OrdersStickersPostRequest.md)|  | [optional] 

### Return type

[**ApiV3OrdersStickersPost200Response**](ApiV3OrdersStickersPost200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список этикеток |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_orders_reshipment_get**
> ApiV3SuppliesOrdersReshipmentGet200Response api_v3_supplies_orders_reshipment_get()

Получить все сборочные задания на повторную отгрузку

Возвращает все сборочные задания, требующие повторной отгрузки. <span class=\"newM\">new</span>

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_orders_reshipment_get200_response import ApiV3SuppliesOrdersReshipmentGet200Response
from wb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wb_client.Configuration(
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
async with wb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wb_client.Api(api_client)

    try:
        # Получить все сборочные задания на повторную отгрузку
        api_response = await api_instance.api_v3_supplies_orders_reshipment_get()
        print("The response of Api->api_v3_supplies_orders_reshipment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->api_v3_supplies_orders_reshipment_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV3SuppliesOrdersReshipmentGet200Response**](ApiV3SuppliesOrdersReshipmentGet200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешно |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

