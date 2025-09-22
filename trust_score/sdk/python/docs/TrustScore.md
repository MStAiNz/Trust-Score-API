# TrustScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** |  | 
**score** | **float** |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.trust_score import TrustScore

# TODO update the JSON string below
json = "{}"
# create an instance of TrustScore from a JSON string
trust_score_instance = TrustScore.from_json(json)
# print the JSON string representation of the object
print(TrustScore.to_json())

# convert the object into a dict
trust_score_dict = trust_score_instance.to_dict()
# create an instance of TrustScore from a dict
trust_score_from_dict = TrustScore.from_dict(trust_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


