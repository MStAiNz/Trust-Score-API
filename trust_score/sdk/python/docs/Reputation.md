# Reputation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** |  | 
**transaction** | **float** |  | [optional] 
**social_signals** | **float** |  | [optional] 
**blockchain** | **float** |  | [optional] 
**score** | **str** |  | [readonly] 
**explanation** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.reputation import Reputation

# TODO update the JSON string below
json = "{}"
# create an instance of Reputation from a JSON string
reputation_instance = Reputation.from_json(json)
# print the JSON string representation of the object
print(Reputation.to_json())

# convert the object into a dict
reputation_dict = reputation_instance.to_dict()
# create an instance of Reputation from a dict
reputation_from_dict = Reputation.from_dict(reputation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


