# Activity

Activities describe any past activity in a site, for example creating an item of content, commenting on a node, liking an item of content. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_person_id** | **str** | The id of the person who performed the activity | 
**id** | **int** | The unique id of the activity | 
**site_id** | **str** | The unique id of the site on which the activity was performed | [optional] 
**posted_at** | **datetime** | The date time at which the activity was performed | [optional] 
**feed_person_id** | **str** | The feed on which this activity was posted | 
**activity_summary** | [**object**](.md) | An object summarizing the activity | [optional] 
**activity_type** | **str** | The type of the activity posted | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


