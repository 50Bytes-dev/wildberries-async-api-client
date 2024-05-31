# wb_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_offices_get**](DefaultApi.md#api_v3_offices_get) | **GET** /api/v3/offices | Получить список складов WB
[**api_v3_passes_get**](DefaultApi.md#api_v3_passes_get) | **GET** /api/v3/passes | Получить список пропусков
[**api_v3_passes_offices_get**](DefaultApi.md#api_v3_passes_offices_get) | **GET** /api/v3/passes/offices | Получить список складов, для которых требуется пропуск
[**api_v3_passes_pass_id_delete**](DefaultApi.md#api_v3_passes_pass_id_delete) | **DELETE** /api/v3/passes/{passId} | Удалить пропуск
[**api_v3_passes_pass_id_put**](DefaultApi.md#api_v3_passes_pass_id_put) | **PUT** /api/v3/passes/{passId} | Обновить пропуск
[**api_v3_passes_post**](DefaultApi.md#api_v3_passes_post) | **POST** /api/v3/passes | Создать пропуск
[**api_v3_stocks_warehouse_id_delete**](DefaultApi.md#api_v3_stocks_warehouse_id_delete) | **DELETE** /api/v3/stocks/{warehouseId} | Удалить остатки товаров
[**api_v3_stocks_warehouse_id_post**](DefaultApi.md#api_v3_stocks_warehouse_id_post) | **POST** /api/v3/stocks/{warehouseId} | Получить остатки товаров
[**api_v3_stocks_warehouse_id_put**](DefaultApi.md#api_v3_stocks_warehouse_id_put) | **PUT** /api/v3/stocks/{warehouseId} | Обновить остатки товаров
[**api_v3_supplies_get**](DefaultApi.md#api_v3_supplies_get) | **GET** /api/v3/supplies | Получить список поставок
[**api_v3_supplies_post**](DefaultApi.md#api_v3_supplies_post) | **POST** /api/v3/supplies | Создать новую поставку
[**api_v3_supplies_supply_id_barcode_get**](DefaultApi.md#api_v3_supplies_supply_id_barcode_get) | **GET** /api/v3/supplies/{supplyId}/barcode | Получить QR поставки
[**api_v3_supplies_supply_id_delete**](DefaultApi.md#api_v3_supplies_supply_id_delete) | **DELETE** /api/v3/supplies/{supplyId} | Удалить поставку
[**api_v3_supplies_supply_id_deliver_patch**](DefaultApi.md#api_v3_supplies_supply_id_deliver_patch) | **PATCH** /api/v3/supplies/{supplyId}/deliver | Передать поставку в доставку
[**api_v3_supplies_supply_id_get**](DefaultApi.md#api_v3_supplies_supply_id_get) | **GET** /api/v3/supplies/{supplyId} | Получить информацию о поставке
[**api_v3_supplies_supply_id_orders_get**](DefaultApi.md#api_v3_supplies_supply_id_orders_get) | **GET** /api/v3/supplies/{supplyId}/orders | Получить сборочные задания в поставке
[**api_v3_supplies_supply_id_orders_order_id_patch**](DefaultApi.md#api_v3_supplies_supply_id_orders_order_id_patch) | **PATCH** /api/v3/supplies/{supplyId}/orders/{orderId} | Добавить к поставке сборочное задание
[**api_v3_supplies_supply_id_trbx_delete**](DefaultApi.md#api_v3_supplies_supply_id_trbx_delete) | **DELETE** /api/v3/supplies/{supplyId}/trbx | Удалить короба из поставки
[**api_v3_supplies_supply_id_trbx_get**](DefaultApi.md#api_v3_supplies_supply_id_trbx_get) | **GET** /api/v3/supplies/{supplyId}/trbx | Получить список коробов поставки
[**api_v3_supplies_supply_id_trbx_post**](DefaultApi.md#api_v3_supplies_supply_id_trbx_post) | **POST** /api/v3/supplies/{supplyId}/trbx | Добавить короба к поставке
[**api_v3_supplies_supply_id_trbx_stickers_post**](DefaultApi.md#api_v3_supplies_supply_id_trbx_stickers_post) | **POST** /api/v3/supplies/{supplyId}/trbx/stickers | Получить стикеры коробов поставки
[**api_v3_supplies_supply_id_trbx_trbx_id_orders_order_id_delete**](DefaultApi.md#api_v3_supplies_supply_id_trbx_trbx_id_orders_order_id_delete) | **DELETE** /api/v3/supplies/{supplyId}/trbx/{trbxId}/orders/{orderId} | Удалить заказ из короба
[**api_v3_supplies_supply_id_trbx_trbx_id_patch**](DefaultApi.md#api_v3_supplies_supply_id_trbx_trbx_id_patch) | **PATCH** /api/v3/supplies/{supplyId}/trbx/{trbxId} | Добавить заказы к коробу
[**api_v3_warehouses_get**](DefaultApi.md#api_v3_warehouses_get) | **GET** /api/v3/warehouses | Получить список складов продавца
[**api_v3_warehouses_post**](DefaultApi.md#api_v3_warehouses_post) | **POST** /api/v3/warehouses | Создать склад продавца
[**api_v3_warehouses_warehouse_id_delete**](DefaultApi.md#api_v3_warehouses_warehouse_id_delete) | **DELETE** /api/v3/warehouses/{warehouseId} | Удалить склад продавца
[**api_v3_warehouses_warehouse_id_put**](DefaultApi.md#api_v3_warehouses_warehouse_id_put) | **PUT** /api/v3/warehouses/{warehouseId} | Обновить склад


# **api_v3_offices_get**
> List[Office] api_v3_offices_get()

Получить список складов WB

Возвращает список всех складов WB для привязки к складам продавца.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.office import Office
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
    api_instance = wb_client.DefaultApi(api_client)

    try:
        # Получить список складов WB
        api_response = await api_instance.api_v3_offices_get()
        print("The response of DefaultApi->api_v3_offices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_offices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Office]**](Office.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список складов WB |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_passes_get**
> List[ModelPass] api_v3_passes_get()

Получить список пропусков

Возвращает список всех пропусков продавца.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.model_pass import ModelPass
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
    api_instance = wb_client.DefaultApi(api_client)

    try:
        # Получить список пропусков
        api_response = await api_instance.api_v3_passes_get()
        print("The response of DefaultApi->api_v3_passes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_passes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ModelPass]**](ModelPass.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список пропусков продавца |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_passes_offices_get**
> List[PassOffice] api_v3_passes_offices_get()

Получить список складов, для которых требуется пропуск

Возвращает список складов для привязки к пропуску продавца. <br> Обратите внимание: данные, которые возвращает метод, могут меняться. Рекомендуем периодически синхронизировать список. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.pass_office import PassOffice
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
    api_instance = wb_client.DefaultApi(api_client)

    try:
        # Получить список складов, для которых требуется пропуск
        api_response = await api_instance.api_v3_passes_offices_get()
        print("The response of DefaultApi->api_v3_passes_offices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_passes_offices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PassOffice]**](PassOffice.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список складов, для которых требуется пропуск. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_passes_pass_id_delete**
> api_v3_passes_pass_id_delete(pass_id)

Удалить пропуск

Удаляет пропуск продавца.

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
    api_instance = wb_client.DefaultApi(api_client)
    pass_id = 45 # int | ID пропуска

    try:
        # Удалить пропуск
        await api_instance.api_v3_passes_pass_id_delete(pass_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_passes_pass_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pass_id** | **int**| ID пропуска | 

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
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_passes_pass_id_put**
> api_v3_passes_pass_id_put(pass_id, api_v3_passes_pass_id_put_request)

Обновить пропуск

Обновляет данные пропуска продавца.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_passes_pass_id_put_request import ApiV3PassesPassIdPutRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    pass_id = 45 # int | ID пропуска
    api_v3_passes_pass_id_put_request = wb_client.ApiV3PassesPassIdPutRequest() # ApiV3PassesPassIdPutRequest | Общая длина ФИО ограничена от 6 до 100 символов. В номере машины могут быть только буквы и цифры.

    try:
        # Обновить пропуск
        await api_instance.api_v3_passes_pass_id_put(pass_id, api_v3_passes_pass_id_put_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_passes_pass_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pass_id** | **int**| ID пропуска | 
 **api_v3_passes_pass_id_put_request** | [**ApiV3PassesPassIdPutRequest**](ApiV3PassesPassIdPutRequest.md)| Общая длина ФИО ограничена от 6 до 100 символов. В номере машины могут быть только буквы и цифры. | 

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
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_passes_post**
> ApiV3PassesPost201Response api_v3_passes_post(api_v3_passes_post_request)

Создать пропуск

Создает пропуск продавца. <br> Пропуск действует 48 часов со времени создания. Метод ограничен одним вызовом в 10 минут. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_passes_post201_response import ApiV3PassesPost201Response
from wb_client.models.api_v3_passes_post_request import ApiV3PassesPostRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    api_v3_passes_post_request = wb_client.ApiV3PassesPostRequest() # ApiV3PassesPostRequest | Общая длина ФИО ограничена от 6 до 100 символов. В номере машины могут быть только буквы и цифры.

    try:
        # Создать пропуск
        api_response = await api_instance.api_v3_passes_post(api_v3_passes_post_request)
        print("The response of DefaultApi->api_v3_passes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_passes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v3_passes_post_request** | [**ApiV3PassesPostRequest**](ApiV3PassesPostRequest.md)| Общая длина ФИО ограничена от 6 до 100 символов. В номере машины могут быть только буквы и цифры. | 

### Return type

[**ApiV3PassesPost201Response**](ApiV3PassesPost201Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_stocks_warehouse_id_delete**
> api_v3_stocks_warehouse_id_delete(warehouse_id, api_v3_stocks_warehouse_id_delete_request)

Удалить остатки товаров

Удаляет остатки товаров. **Внимание! Действие необратимо**. Удаленный остаток будет необходимо загрузить повторно для возобновления продаж.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_stocks_warehouse_id_delete_request import ApiV3StocksWarehouseIdDeleteRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    warehouse_id = 1 # int | ID склада продавца
    api_v3_stocks_warehouse_id_delete_request = wb_client.ApiV3StocksWarehouseIdDeleteRequest() # ApiV3StocksWarehouseIdDeleteRequest | 

    try:
        # Удалить остатки товаров
        await api_instance.api_v3_stocks_warehouse_id_delete(warehouse_id, api_v3_stocks_warehouse_id_delete_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_stocks_warehouse_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| ID склада продавца | 
 **api_v3_stocks_warehouse_id_delete_request** | [**ApiV3StocksWarehouseIdDeleteRequest**](ApiV3StocksWarehouseIdDeleteRequest.md)|  | 

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
**204** | Удалено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Не найдены запрашиваемые данные |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_stocks_warehouse_id_post**
> ApiV3StocksWarehouseIdPost200Response api_v3_stocks_warehouse_id_post(warehouse_id, api_v3_stocks_warehouse_id_post_request)

Получить остатки товаров

Возвращает остатки товаров.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_stocks_warehouse_id_post200_response import ApiV3StocksWarehouseIdPost200Response
from wb_client.models.api_v3_stocks_warehouse_id_post_request import ApiV3StocksWarehouseIdPostRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    warehouse_id = 1 # int | ID склада продавца
    api_v3_stocks_warehouse_id_post_request = wb_client.ApiV3StocksWarehouseIdPostRequest() # ApiV3StocksWarehouseIdPostRequest | 

    try:
        # Получить остатки товаров
        api_response = await api_instance.api_v3_stocks_warehouse_id_post(warehouse_id, api_v3_stocks_warehouse_id_post_request)
        print("The response of DefaultApi->api_v3_stocks_warehouse_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_stocks_warehouse_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| ID склада продавца | 
 **api_v3_stocks_warehouse_id_post_request** | [**ApiV3StocksWarehouseIdPostRequest**](ApiV3StocksWarehouseIdPostRequest.md)|  | 

### Return type

[**ApiV3StocksWarehouseIdPost200Response**](ApiV3StocksWarehouseIdPost200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список остатков |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_stocks_warehouse_id_put**
> api_v3_stocks_warehouse_id_put(warehouse_id, api_v3_stocks_warehouse_id_put_request=api_v3_stocks_warehouse_id_put_request)

Обновить остатки товаров

Обновляет остатки товаров. <br> `Важно!` Имена параметров запроса не валидируются. При отправке некорректных имен Вы получите успешный ответ(204), но остатки не обновятся.<br> Тщательнее проверяйте данные перед отправкой. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_stocks_warehouse_id_put_request import ApiV3StocksWarehouseIdPutRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    warehouse_id = 1 # int | ID склада продавца
    api_v3_stocks_warehouse_id_put_request = wb_client.ApiV3StocksWarehouseIdPutRequest() # ApiV3StocksWarehouseIdPutRequest |  (optional)

    try:
        # Обновить остатки товаров
        await api_instance.api_v3_stocks_warehouse_id_put(warehouse_id, api_v3_stocks_warehouse_id_put_request=api_v3_stocks_warehouse_id_put_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_stocks_warehouse_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| ID склада продавца | 
 **api_v3_stocks_warehouse_id_put_request** | [**ApiV3StocksWarehouseIdPutRequest**](ApiV3StocksWarehouseIdPutRequest.md)|  | [optional] 

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
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | Ошибка обновления остатков |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_get**
> ApiV3SuppliesGet200Response api_v3_supplies_get(limit, next)

Получить список поставок

Возвращает список поставок. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_get200_response import ApiV3SuppliesGet200Response
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
    api_instance = wb_client.DefaultApi(api_client)
    limit = 56 # int | Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
    next = 56 # int | Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных. Для получения полного списка данных должен быть равен 0 в первом запросе. Для следующих запросов необходимо брать значения из одноимённого поля в ответе.

    try:
        # Получить список поставок
        api_response = await api_instance.api_v3_supplies_get(limit, next)
        print("The response of DefaultApi->api_v3_supplies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Параметр пагинации. Устанавливает предельное количество возвращаемых данных. | 
 **next** | **int**| Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных. Для получения полного списка данных должен быть равен 0 в первом запросе. Для следующих запросов необходимо брать значения из одноимённого поля в ответе. | 

### Return type

[**ApiV3SuppliesGet200Response**](ApiV3SuppliesGet200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список поставок |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_post**
> ApiV3SuppliesPost201Response api_v3_supplies_post(api_v3_supplies_post_request)

Создать новую поставку

**Ограничения работы с поставками**:  - Только для сборочных заданий по схеме \"Везу на склад WB\" - При добавлении в поставку все передаваемые сборочные задания в статусе **new** (\"Новое\") будут автоматически переведены в статус **confirm** (\"На сборке\"). - Обратите внимание, что если вы переведёте сборочное задание в статус **cancel** (\"Отмена продавцом\"), то сборочное задание автоматически удалится из поставки, если было прикреплено к ней. - Поставку можно собрать только из сборочных заданий (заказов) одного габаритного типа (cargoType). Новая поставка не обладает габаритным признаком. При добавлении первого заказа в поставку она приобретает габаритный признак этого заказа. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_post201_response import ApiV3SuppliesPost201Response
from wb_client.models.api_v3_supplies_post_request import ApiV3SuppliesPostRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    api_v3_supplies_post_request = wb_client.ApiV3SuppliesPostRequest() # ApiV3SuppliesPostRequest | 

    try:
        # Создать новую поставку
        api_response = await api_instance.api_v3_supplies_post(api_v3_supplies_post_request)
        print("The response of DefaultApi->api_v3_supplies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v3_supplies_post_request** | [**ApiV3SuppliesPostRequest**](ApiV3SuppliesPostRequest.md)|  | 

### Return type

[**ApiV3SuppliesPost201Response**](ApiV3SuppliesPost201Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Создано |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_barcode_get**
> ApiV3SuppliesSupplyIdBarcodeGet200Response api_v3_supplies_supply_id_barcode_get(supply_id, type)

Получить QR поставки

Возвращает QR в svg, zplv (вертикальный), zplh (горизонтальный), png. <br> Можно получить, только если поставка передана в доставку. <dt>Доступные размеры:</dt> <dd>580x400 пикселей 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_supply_id_barcode_get200_response import ApiV3SuppliesSupplyIdBarcodeGet200Response
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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки
    type = 'type_example' # str | Тип этикетки

    try:
        # Получить QR поставки
        api_response = await api_instance.api_v3_supplies_supply_id_barcode_get(supply_id, type)
        print("The response of DefaultApi->api_v3_supplies_supply_id_barcode_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_barcode_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 
 **type** | **str**| Тип этикетки | 

### Return type

[**ApiV3SuppliesSupplyIdBarcodeGet200Response**](ApiV3SuppliesSupplyIdBarcodeGet200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QR поставки |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | Ошибка запроса данных |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_delete**
> api_v3_supplies_supply_id_delete(supply_id)

Удалить поставку

Удаляет поставку, если она активна и за ней не закреплено ни одно сборочное задание.

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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки

    try:
        # Удалить поставку
        await api_instance.api_v3_supplies_supply_id_delete(supply_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 

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
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | За поставкой закреплены сборочные задания |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_deliver_patch**
> api_v3_supplies_supply_id_deliver_patch(supply_id)

Передать поставку в доставку

Закрывает поставку и переводит все сборочные задания в ней в статус **complete** (\"В доставке\"). После закрытия поставки новые сборочные задания к ней добавить будет невозможно. Передать поставку в доставку можно только при наличии в ней хотя бы одного сборочного задания и отсутствии пустых коробов. 

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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки

    try:
        # Передать поставку в доставку
        await api_instance.api_v3_supplies_supply_id_deliver_patch(supply_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_deliver_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 

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
**204** | Передано в доставку |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | Ошибка закрытия поставки |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_get**
> Supply api_v3_supplies_supply_id_get(supply_id)

Получить информацию о поставке

Возвращает информацию о поставке. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.supply import Supply
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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки

    try:
        # Получить информацию о поставке
        api_response = await api_instance.api_v3_supplies_supply_id_get(supply_id)
        print("The response of DefaultApi->api_v3_supplies_supply_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 

### Return type

[**Supply**](Supply.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о поставке |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_orders_get**
> ApiV3SuppliesSupplyIdOrdersGet200Response api_v3_supplies_supply_id_orders_get(supply_id)

Получить сборочные задания в поставке

Возвращает сборочные задания, закреплённые за поставкой. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_supply_id_orders_get200_response import ApiV3SuppliesSupplyIdOrdersGet200Response
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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки

    try:
        # Получить сборочные задания в поставке
        api_response = await api_instance.api_v3_supplies_supply_id_orders_get(supply_id)
        print("The response of DefaultApi->api_v3_supplies_supply_id_orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_orders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 

### Return type

[**ApiV3SuppliesSupplyIdOrdersGet200Response**](ApiV3SuppliesSupplyIdOrdersGet200Response.md)

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
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_orders_order_id_patch**
> api_v3_supplies_supply_id_orders_order_id_patch(supply_id, order_id)

Добавить к поставке сборочное задание

Добавляет к поставке сборочное задание и переводит его в статус **confirm** (\"На сборке\").  <br> Также может перемещать сборочное задание между активными поставками, либо из закрытой в активную при условии, что сборочное задание требует повторной отгрузки. <br> <br> `Важно!` <br> В пустую поставку можно добавить сборочное задание любого габаритного типа. <br> После добавления первого задания поставка приобретает габаритный тип этого задания, см. значение поля `cargoType` в ответе метода <b>\"Получить информацию о поставке\"</b>. <br> После этого добавить в поставку можно только те задания, габаритный тип которых соответствует таковому у поставки. 

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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки
    order_id = 5632423 # int | ID сборочного задания

    try:
        # Добавить к поставке сборочное задание
        await api_instance.api_v3_supplies_supply_id_orders_order_id_patch(supply_id, order_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_orders_order_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 
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
**204** | Задание закреплено за поставкой |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | Ошибка добавления сборочного задания к поставке |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_trbx_delete**
> api_v3_supplies_supply_id_trbx_delete(supply_id, api_v3_supplies_supply_id_trbx_delete_request=api_v3_supplies_supply_id_trbx_delete_request)

Удалить короба из поставки

Убирает заказы из перечисленных коробов поставки и удаляет короба. Можно удалить, только пока поставка на сборке.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_supply_id_trbx_delete_request import ApiV3SuppliesSupplyIdTrbxDeleteRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки
    api_v3_supplies_supply_id_trbx_delete_request = wb_client.ApiV3SuppliesSupplyIdTrbxDeleteRequest() # ApiV3SuppliesSupplyIdTrbxDeleteRequest |  (optional)

    try:
        # Удалить короба из поставки
        await api_instance.api_v3_supplies_supply_id_trbx_delete(supply_id, api_v3_supplies_supply_id_trbx_delete_request=api_v3_supplies_supply_id_trbx_delete_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_trbx_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 
 **api_v3_supplies_supply_id_trbx_delete_request** | [**ApiV3SuppliesSupplyIdTrbxDeleteRequest**](ApiV3SuppliesSupplyIdTrbxDeleteRequest.md)|  | [optional] 

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
**204** | Удалено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_trbx_get**
> ApiV3SuppliesSupplyIdTrbxGet200Response api_v3_supplies_supply_id_trbx_get(supply_id)

Получить список коробов поставки

Возвращает список коробов и идентификаторы заказов, входящих в них. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_supply_id_trbx_get200_response import ApiV3SuppliesSupplyIdTrbxGet200Response
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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки

    try:
        # Получить список коробов поставки
        api_response = await api_instance.api_v3_supplies_supply_id_trbx_get(supply_id)
        print("The response of DefaultApi->api_v3_supplies_supply_id_trbx_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_trbx_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 

### Return type

[**ApiV3SuppliesSupplyIdTrbxGet200Response**](ApiV3SuppliesSupplyIdTrbxGet200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список коробов |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_trbx_post**
> ApiV3SuppliesSupplyIdTrbxPost201Response api_v3_supplies_supply_id_trbx_post(supply_id, api_v3_supplies_supply_id_trbx_post_request=api_v3_supplies_supply_id_trbx_post_request)

Добавить короба к поставке

Добавляет требуемое количество коробов в поставку. Можно добавить, только пока поставка на сборке.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_supply_id_trbx_post201_response import ApiV3SuppliesSupplyIdTrbxPost201Response
from wb_client.models.api_v3_supplies_supply_id_trbx_post_request import ApiV3SuppliesSupplyIdTrbxPostRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки
    api_v3_supplies_supply_id_trbx_post_request = wb_client.ApiV3SuppliesSupplyIdTrbxPostRequest() # ApiV3SuppliesSupplyIdTrbxPostRequest |  (optional)

    try:
        # Добавить короба к поставке
        api_response = await api_instance.api_v3_supplies_supply_id_trbx_post(supply_id, api_v3_supplies_supply_id_trbx_post_request=api_v3_supplies_supply_id_trbx_post_request)
        print("The response of DefaultApi->api_v3_supplies_supply_id_trbx_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_trbx_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 
 **api_v3_supplies_supply_id_trbx_post_request** | [**ApiV3SuppliesSupplyIdTrbxPostRequest**](ApiV3SuppliesSupplyIdTrbxPostRequest.md)|  | [optional] 

### Return type

[**ApiV3SuppliesSupplyIdTrbxPost201Response**](ApiV3SuppliesSupplyIdTrbxPost201Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Создано |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** |  |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_trbx_stickers_post**
> ApiV3SuppliesSupplyIdTrbxStickersPost200Response api_v3_supplies_supply_id_trbx_stickers_post(supply_id, type, api_v3_supplies_supply_id_trbx_stickers_post_request=api_v3_supplies_supply_id_trbx_stickers_post_request)

Получить стикеры коробов поставки

Возвращает стикеры QR в svg, zplv (вертикальный), zplh (горизонтальный), png.<br> Можно получить, только если в коробе есть заказы. <dt>Размер стикеров: 580x400 пикселей</dt> 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_supply_id_trbx_stickers_post200_response import ApiV3SuppliesSupplyIdTrbxStickersPost200Response
from wb_client.models.api_v3_supplies_supply_id_trbx_stickers_post_request import ApiV3SuppliesSupplyIdTrbxStickersPostRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки
    type = 'type_example' # str | Тип этикетки
    api_v3_supplies_supply_id_trbx_stickers_post_request = wb_client.ApiV3SuppliesSupplyIdTrbxStickersPostRequest() # ApiV3SuppliesSupplyIdTrbxStickersPostRequest |  (optional)

    try:
        # Получить стикеры коробов поставки
        api_response = await api_instance.api_v3_supplies_supply_id_trbx_stickers_post(supply_id, type, api_v3_supplies_supply_id_trbx_stickers_post_request=api_v3_supplies_supply_id_trbx_stickers_post_request)
        print("The response of DefaultApi->api_v3_supplies_supply_id_trbx_stickers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_trbx_stickers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 
 **type** | **str**| Тип этикетки | 
 **api_v3_supplies_supply_id_trbx_stickers_post_request** | [**ApiV3SuppliesSupplyIdTrbxStickersPostRequest**](ApiV3SuppliesSupplyIdTrbxStickersPostRequest.md)|  | [optional] 

### Return type

[**ApiV3SuppliesSupplyIdTrbxStickersPost200Response**](ApiV3SuppliesSupplyIdTrbxStickersPost200Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Стикеры коробов |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_trbx_trbx_id_orders_order_id_delete**
> api_v3_supplies_supply_id_trbx_trbx_id_orders_order_id_delete(supply_id, trbx_id, order_id)

Удалить заказ из короба

Удаляет заказ из короба выбранной поставки. Можно удалить, только пока поставка на сборке.

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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки
    trbx_id = 'WB-TRBX-1234567' # str | ID короба
    order_id = 5632423 # int | ID сборочного задания

    try:
        # Удалить заказ из короба
        await api_instance.api_v3_supplies_supply_id_trbx_trbx_id_orders_order_id_delete(supply_id, trbx_id, order_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_trbx_trbx_id_orders_order_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 
 **trbx_id** | **str**| ID короба | 
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
**204** | Удалено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_supplies_supply_id_trbx_trbx_id_patch**
> api_v3_supplies_supply_id_trbx_trbx_id_patch(supply_id, trbx_id, api_v3_supplies_supply_id_trbx_trbx_id_patch_request=api_v3_supplies_supply_id_trbx_trbx_id_patch_request)

Добавить заказы к коробу

Добавляет заказы в короб для выбранной поставки. Можно добавить, только пока поставка на сборке.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_supplies_supply_id_trbx_trbx_id_patch_request import ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    supply_id = 'WB-GI-1234567' # str | ID поставки
    trbx_id = 'WB-TRBX-1234567' # str | ID короба
    api_v3_supplies_supply_id_trbx_trbx_id_patch_request = wb_client.ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest() # ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest |  (optional)

    try:
        # Добавить заказы к коробу
        await api_instance.api_v3_supplies_supply_id_trbx_trbx_id_patch(supply_id, trbx_id, api_v3_supplies_supply_id_trbx_trbx_id_patch_request=api_v3_supplies_supply_id_trbx_trbx_id_patch_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_supplies_supply_id_trbx_trbx_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_id** | **str**| ID поставки | 
 **trbx_id** | **str**| ID короба | 
 **api_v3_supplies_supply_id_trbx_trbx_id_patch_request** | [**ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest**](ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest.md)|  | [optional] 

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
**204** | Добавлено |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_warehouses_get**
> List[Warehouse] api_v3_warehouses_get()

Получить список складов продавца

Возвращает список всех складов продавца.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.warehouse import Warehouse
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
    api_instance = wb_client.DefaultApi(api_client)

    try:
        # Получить список складов продавца
        api_response = await api_instance.api_v3_warehouses_get()
        print("The response of DefaultApi->api_v3_warehouses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_warehouses_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Warehouse]**](Warehouse.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список складов продавца |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_warehouses_post**
> ApiV3WarehousesPost201Response api_v3_warehouses_post(api_v3_warehouses_post_request)

Создать склад продавца

Создает склад продавца. Нельзя привязывать склад WB, который уже используется.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_warehouses_post201_response import ApiV3WarehousesPost201Response
from wb_client.models.api_v3_warehouses_post_request import ApiV3WarehousesPostRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    api_v3_warehouses_post_request = wb_client.ApiV3WarehousesPostRequest() # ApiV3WarehousesPostRequest | 

    try:
        # Создать склад продавца
        api_response = await api_instance.api_v3_warehouses_post(api_v3_warehouses_post_request)
        print("The response of DefaultApi->api_v3_warehouses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_warehouses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v3_warehouses_post_request** | [**ApiV3WarehousesPostRequest**](ApiV3WarehousesPostRequest.md)|  | 

### Return type

[**ApiV3WarehousesPost201Response**](ApiV3WarehousesPost201Response.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Создано |  -  |
**400** | Запрос содержит некорректные данные. Проверьте его на соответствие документации. |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | Ошибка создания нового склада |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_warehouses_warehouse_id_delete**
> api_v3_warehouses_warehouse_id_delete(warehouse_id)

Удалить склад продавца

Удаляет склад продавца.

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
    api_instance = wb_client.DefaultApi(api_client)
    warehouse_id = 1 # int | ID склада продавца

    try:
        # Удалить склад продавца
        await api_instance.api_v3_warehouses_warehouse_id_delete(warehouse_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_warehouses_warehouse_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| ID склада продавца | 

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
**401** | Пользователь не авторизован |  -  |
**403** | Доступ запрещён |  -  |
**404** | Запрашиваемый ресурс не найден |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_warehouses_warehouse_id_put**
> api_v3_warehouses_warehouse_id_put(warehouse_id, api_v3_warehouses_warehouse_id_put_request)

Обновить склад

Обновляет склад продавца. Изменение выбранного склада WB допустимо раз в сутки. Нельзя привязывать склад WB, который уже используется.

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wb_client
from wb_client.models.api_v3_warehouses_warehouse_id_put_request import ApiV3WarehousesWarehouseIdPutRequest
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
    api_instance = wb_client.DefaultApi(api_client)
    warehouse_id = 1 # int | ID склада продавца
    api_v3_warehouses_warehouse_id_put_request = wb_client.ApiV3WarehousesWarehouseIdPutRequest() # ApiV3WarehousesWarehouseIdPutRequest | 

    try:
        # Обновить склад
        await api_instance.api_v3_warehouses_warehouse_id_put(warehouse_id, api_v3_warehouses_warehouse_id_put_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v3_warehouses_warehouse_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| ID склада продавца | 
 **api_v3_warehouses_warehouse_id_put_request** | [**ApiV3WarehousesWarehouseIdPutRequest**](ApiV3WarehousesWarehouseIdPutRequest.md)|  | 

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
**404** | Запрашиваемый ресурс не найден |  -  |
**409** | Ошибка обновления склада |  -  |
**429** | Превышен лимит по запросам |  -  |
**500** | Внутренняя ошибка сервиса |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

