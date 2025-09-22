# openapi_client.ApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_reputation_collect_create**](ApiApi.md#api_reputation_collect_create) | **POST** /api/reputation/collect/{user_id}/ | 
[**api_reputation_reputation_list**](ApiApi.md#api_reputation_reputation_list) | **GET** /api/reputation/reputation/ | 
[**api_reputation_reputation_retrieve**](ApiApi.md#api_reputation_reputation_retrieve) | **GET** /api/reputation/reputation/{id}/ | 
[**api_reputation_retrieve**](ApiApi.md#api_reputation_retrieve) | **GET** /api/reputation/{user_id}/ | 
[**api_schema_retrieve**](ApiApi.md#api_schema_retrieve) | **GET** /api/schema/ | 
[**api_token_create**](ApiApi.md#api_token_create) | **POST** /api/token/ | 
[**api_token_refresh_create**](ApiApi.md#api_token_refresh_create) | **POST** /api/token/refresh/ | 


# **api_reputation_collect_create**
> api_reputation_collect_create(user_id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiApi(api_client)
    user_id = 56 # int | 

    try:
        api_instance.api_reputation_collect_create(user_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_reputation_collect_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_reputation_reputation_list**
> List[Reputation] api_reputation_reputation_list()

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.reputation import Reputation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiApi(api_client)

    try:
        api_response = api_instance.api_reputation_reputation_list()
        print("The response of ApiApi->api_reputation_reputation_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_reputation_reputation_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Reputation]**](Reputation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_reputation_reputation_retrieve**
> Reputation api_reputation_reputation_retrieve(id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.reputation import Reputation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiApi(api_client)
    id = 56 # int | A unique integer value identifying this reputation.

    try:
        api_response = api_instance.api_reputation_reputation_retrieve(id)
        print("The response of ApiApi->api_reputation_reputation_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_reputation_reputation_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this reputation. | 

### Return type

[**Reputation**](Reputation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_reputation_retrieve**
> TrustScore api_reputation_retrieve(user_id)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.trust_score import TrustScore
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiApi(api_client)
    user_id = 56 # int | 

    try:
        api_response = api_instance.api_reputation_retrieve(user_id)
        print("The response of ApiApi->api_reputation_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_reputation_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**TrustScore**](TrustScore.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_schema_retrieve**
> Dict[str, object] api_schema_retrieve(format=format, lang=lang)

OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiApi(api_client)
    format = 'format_example' # str |  (optional)
    lang = 'lang_example' # str |  (optional)

    try:
        api_response = api_instance.api_schema_retrieve(format=format, lang=lang)
        print("The response of ApiApi->api_schema_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_schema_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 
 **lang** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.oai.openapi, application/yaml, application/vnd.oai.openapi+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_create**
> TokenObtainPair api_token_create(token_obtain_pair)

Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

### Example


```python
import openapi_client
from openapi_client.models.token_obtain_pair import TokenObtainPair
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiApi(api_client)
    token_obtain_pair = openapi_client.TokenObtainPair() # TokenObtainPair | 

    try:
        api_response = api_instance.api_token_create(token_obtain_pair)
        print("The response of ApiApi->api_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_obtain_pair** | [**TokenObtainPair**](TokenObtainPair.md)|  | 

### Return type

[**TokenObtainPair**](TokenObtainPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_refresh_create**
> TokenRefresh api_token_refresh_create(token_refresh)

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

### Example


```python
import openapi_client
from openapi_client.models.token_refresh import TokenRefresh
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiApi(api_client)
    token_refresh = openapi_client.TokenRefresh() # TokenRefresh | 

    try:
        api_response = api_instance.api_token_refresh_create(token_refresh)
        print("The response of ApiApi->api_token_refresh_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_token_refresh_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_refresh** | [**TokenRefresh**](TokenRefresh.md)|  | 

### Return type

[**TokenRefresh**](TokenRefresh.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

