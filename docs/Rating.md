# Rating

A person can rate an item of content by liking it. They can also remove their like of an item of content. API methods exist to get a list of ratings and to add a new rating. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**aggregate** | [**RatingAggregate**](RatingAggregate.md) |  | 
**rated_at** | **datetime** |  | [optional] 
**my_rating** | **str** | The rating. The type is specific to the rating scheme, boolean for the likes and an integer for the fiveStar. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


