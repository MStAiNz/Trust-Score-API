# TokenObtainPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**access** | **str** |  | [readonly] 
**refresh** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.token_obtain_pair import TokenObtainPair

# TODO update the JSON string below
json = "{}"
# create an instance of TokenObtainPair from a JSON string
token_obtain_pair_instance = TokenObtainPair.from_json(json)
# print the JSON string representation of the object
print(TokenObtainPair.to_json())

# convert the object into a dict
token_obtain_pair_dict = token_obtain_pair_instance.to_dict()
# create an instance of TokenObtainPair from a dict
token_obtain_pair_from_dict = TokenObtainPair.from_dict(token_obtain_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


