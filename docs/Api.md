# wildberries_async_api_client.Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adv_v0_active_get**](Api.md#adv_v0_active_get) | **GET** /adv/v0/active | Изменение активности предметной группы
[**adv_v1_search_set_excluded_post**](Api.md#adv_v1_search_set_excluded_post) | **POST** /adv/v1/search/set-excluded | Установка/удаление минус-фраз из поиска
[**adv_v1_search_set_phrase_post**](Api.md#adv_v1_search_set_phrase_post) | **POST** /adv/v1/search/set-phrase | Установка/удаление минус-фраз фразового соответствия
[**adv_v1_search_set_plus_get**](Api.md#adv_v1_search_set_plus_get) | **GET** /adv/v1/search/set-plus | Управление активностью фиксированных фраз
[**adv_v1_search_set_plus_post**](Api.md#adv_v1_search_set_plus_post) | **POST** /adv/v1/search/set-plus | Установка/удаление фиксированных фраз
[**adv_v1_search_set_strong_post**](Api.md#adv_v1_search_set_strong_post) | **POST** /adv/v1/search/set-strong | Установка/удаление минус-фраз точного соответствия
[**adv_v1_search_supplier_products_get**](Api.md#adv_v1_search_supplier_products_get) | **GET** /adv/v1/search/supplier-products | Список товаров для кампании в поиске
[**adv_v1_search_supplier_subjects_get**](Api.md#adv_v1_search_supplier_subjects_get) | **GET** /adv/v1/search/supplier-subjects | Список предметов для кампании в поиске


# **adv_v0_active_get**
> adv_v0_active_get(id, subject_id, status)

Изменение активности предметной группы

Изменяет активность предметной группы. Только для кампаний:   * в поиске и поиск + каталог;   * со статусами Идут показы (`9`) и Кампания на паузе (`11`). Максимум 5 запросов в секунду. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
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
    api_instance = wildberries_async_api_client.Api(api_client)
    id = 1234 # int | Идентификатор кампании
    subject_id = 1234 # int | Идентификатор предметной группы, для которой меняется активность
    status = 'true' # str | Новое состояние (`true` - сделать группу активной или `false` - сделать группу неактивной)

    try:
        # Изменение активности предметной группы
        await api_instance.adv_v0_active_get(id, subject_id, status)
    except Exception as e:
        print("Exception when calling Api->adv_v0_active_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Идентификатор кампании | 
 **subject_id** | **int**| Идентификатор предметной группы, для которой меняется активность | 
 **status** | **str**| Новое состояние (&#x60;true&#x60; - сделать группу активной или &#x60;false&#x60; - сделать группу неактивной) | 

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
**200** | Статус изменен |  -  |
**400** | Статус не изменен |  -  |
**401** | Не авторизован |  -  |
**422** | Размер ставки не изменен |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adv_v1_search_set_excluded_post**
> adv_v1_search_set_excluded_post(id, adv_v1_search_set_excluded_post_request)

Установка/удаление минус-фраз из поиска

Устанавливает и удаляет минус-фразы из поиска. Только для кампаний в поиске и поиск + каталог.<br>  Максимально допустимое количество минус-фраз в кампании - 1000 шт. <br>  Отправка пустого массива удаляет все минус-фразы из поиска из кампании.  Максимум 2 запроса в секунду.       

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.adv_v1_search_set_excluded_post_request import AdvV1SearchSetExcludedPostRequest
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
    api_instance = wildberries_async_api_client.Api(api_client)
    id = 1234567 # int | Идентификатор кампании
    adv_v1_search_set_excluded_post_request = {"excluded":["что-то синее","картошечка"]} # AdvV1SearchSetExcludedPostRequest | 

    try:
        # Установка/удаление минус-фраз из поиска
        await api_instance.adv_v1_search_set_excluded_post(id, adv_v1_search_set_excluded_post_request)
    except Exception as e:
        print("Exception when calling Api->adv_v1_search_set_excluded_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Идентификатор кампании | 
 **adv_v1_search_set_excluded_post_request** | [**AdvV1SearchSetExcludedPostRequest**](AdvV1SearchSetExcludedPostRequest.md)|  | 

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
**200** |  |  -  |
**400** |  |  -  |
**401** | Не авторизован |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adv_v1_search_set_phrase_post**
> adv_v1_search_set_phrase_post(id, adv_v1_search_set_phrase_post_request)

Установка/удаление минус-фраз фразового соответствия

Устанавливает и удаляет минус-фразы фразового соответствия. Только для кампаний в поиске и поиск + каталог.<br>  Максимально допустимое количество минус-фраз в кампании - 1000 шт.<br>  Отправка пустого массива удаляет все минус-фразы фразового соответствия из кампании.  Максимум 2 запроса в секунду. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.adv_v1_search_set_phrase_post_request import AdvV1SearchSetPhrasePostRequest
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
    api_instance = wildberries_async_api_client.Api(api_client)
    id = 1234567 # int | Идентификатор кампании
    adv_v1_search_set_phrase_post_request = {"phrase":["сло","гу"]} # AdvV1SearchSetPhrasePostRequest | 

    try:
        # Установка/удаление минус-фраз фразового соответствия
        await api_instance.adv_v1_search_set_phrase_post(id, adv_v1_search_set_phrase_post_request)
    except Exception as e:
        print("Exception when calling Api->adv_v1_search_set_phrase_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Идентификатор кампании | 
 **adv_v1_search_set_phrase_post_request** | [**AdvV1SearchSetPhrasePostRequest**](AdvV1SearchSetPhrasePostRequest.md)|  | 

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
**200** |  |  -  |
**400** |  |  -  |
**401** | Не авторизован |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adv_v1_search_set_plus_get**
> adv_v1_search_set_plus_get(id, fixed=fixed)

Управление активностью фиксированных фраз

Изменяет активность фиксированных фраз. Только для кампаний в поиске и поиск + каталог.  Максимум 1 запрос в 500 миллисекунд. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
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
    api_instance = wildberries_async_api_client.Api(api_client)
    id = 1234567 # int | Идентификатор кампании
    fixed = True # bool | Новое состояние (`false` - сделать неактивными, `true` - сделать активными) (optional)

    try:
        # Управление активностью фиксированных фраз
        await api_instance.adv_v1_search_set_plus_get(id, fixed=fixed)
    except Exception as e:
        print("Exception when calling Api->adv_v1_search_set_plus_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Идентификатор кампании | 
 **fixed** | **bool**| Новое состояние (&#x60;false&#x60; - сделать неактивными, &#x60;true&#x60; - сделать активными) | [optional] 

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
**200** | Активность изменена |  -  |
**400** | Активность фиксированных фраз не изменена |  -  |
**401** | Не авторизован |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adv_v1_search_set_plus_post**
> List[str] adv_v1_search_set_plus_post(id, adv_v1_search_set_plus_post_request)

Установка/удаление фиксированных фраз

Устанавливает и удаляет фиксированные фразы. Только для кампаний в поиске и поиск + каталог.  Отправка пустого массива удаляет все фиксированные фразы и отключает активность фиксированных фраз в кампании. Максимум 1 запрос в 500 миллисекунд. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.adv_v1_search_set_plus_post_request import AdvV1SearchSetPlusPostRequest
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
    api_instance = wildberries_async_api_client.Api(api_client)
    id = 1234567 # int | Идентификатор кампании
    adv_v1_search_set_plus_post_request = {"pluse":["Фраза 1","Фраза 2"]} # AdvV1SearchSetPlusPostRequest | 

    try:
        # Установка/удаление фиксированных фраз
        api_response = await api_instance.adv_v1_search_set_plus_post(id, adv_v1_search_set_plus_post_request)
        print("The response of Api->adv_v1_search_set_plus_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->adv_v1_search_set_plus_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Идентификатор кампании | 
 **adv_v1_search_set_plus_post_request** | [**AdvV1SearchSetPlusPostRequest**](AdvV1SearchSetPlusPostRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешно |  -  |
**400** | Некорректный запрос |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adv_v1_search_set_strong_post**
> adv_v1_search_set_strong_post(id, adv_v1_search_set_strong_post_request)

Установка/удаление минус-фраз точного соответствия

Устанавливает и удаляет минус-фразы точного соответствия. Только для кампаний в поиске и поиск + каталог.<br>  Максимально допустимое количество минус-фраз в кампании - 1000 шт. <br>  Отправка пустого массива удаляет все минус-фразы точного соответствия из кампании.  Максимум 2 запроса в секунду. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.adv_v1_search_set_strong_post_request import AdvV1SearchSetStrongPostRequest
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
    api_instance = wildberries_async_api_client.Api(api_client)
    id = 1234567 # int | Идентификатор кампании
    adv_v1_search_set_strong_post_request = {"strong":["стоять","лопата"]} # AdvV1SearchSetStrongPostRequest | 

    try:
        # Установка/удаление минус-фраз точного соответствия
        await api_instance.adv_v1_search_set_strong_post(id, adv_v1_search_set_strong_post_request)
    except Exception as e:
        print("Exception when calling Api->adv_v1_search_set_strong_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Идентификатор кампании | 
 **adv_v1_search_set_strong_post_request** | [**AdvV1SearchSetStrongPostRequest**](AdvV1SearchSetStrongPostRequest.md)|  | 

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
**200** |  |  -  |
**400** |  |  -  |
**401** | Не авторизован |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adv_v1_search_supplier_products_get**
> List[AdvV1SearchSupplierProductsGet200ResponseInner] adv_v1_search_supplier_products_get(subject=subject)

Список товаров для кампании в поиске

Метод возвращает список товаров, которые есть в наличии. Эти товары можно добавить в кампанию.  <br> Допускается  1 запрос в 12 секунд.<br>  Чтобы получить все товары, которые есть в наличии, необходимо отправить запрос без параметра <code>subject</code>. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.adv_v1_search_supplier_products_get200_response_inner import AdvV1SearchSupplierProductsGet200ResponseInner
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
    api_instance = wildberries_async_api_client.Api(api_client)
    subject = 56 # int | ID предмета (optional)

    try:
        # Список товаров для кампании в поиске
        api_response = await api_instance.adv_v1_search_supplier_products_get(subject=subject)
        print("The response of Api->adv_v1_search_supplier_products_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->adv_v1_search_supplier_products_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **int**| ID предмета | [optional] 

### Return type

[**List[AdvV1SearchSupplierProductsGet200ResponseInner]**](AdvV1SearchSupplierProductsGet200ResponseInner.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** | Не авторизован |  -  |
**429** | Превышен лимит по запросам |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adv_v1_search_supplier_subjects_get**
> List[AdvV1SearchSupplierSubjectsGet200ResponseInner] adv_v1_search_supplier_subjects_get()

Список предметов для кампании в поиске

Метод позволяет получать список предметов продавца и количество артикулов WB по каждому предмету.    <br> Допускается 1 запрос в 12 секунд. 

### Example

* Api Key Authentication (HeaderApiKey):

```python
import wildberries_async_api_client
from wildberries_async_api_client.models.adv_v1_search_supplier_subjects_get200_response_inner import AdvV1SearchSupplierSubjectsGet200ResponseInner
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
    api_instance = wildberries_async_api_client.Api(api_client)

    try:
        # Список предметов для кампании в поиске
        api_response = await api_instance.adv_v1_search_supplier_subjects_get()
        print("The response of Api->adv_v1_search_supplier_subjects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Api->adv_v1_search_supplier_subjects_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AdvV1SearchSupplierSubjectsGet200ResponseInner]**](AdvV1SearchSupplierSubjectsGet200ResponseInner.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Не авторизован |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

