# PersonNetwork

A network is the group of users and sites that belong to an organization. Networks are organized by email domain. When a user signs up for an Alfresco account , their email domain becomes their Home Network. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This network&#39;s unique id | 
**home_network** | **bool** | Is this the home network? | [optional] 
**is_enabled** | **bool** |  | 
**created_at** | **datetime** |  | [optional] 
**paid_network** | **bool** |  | [optional] 
**subscription_level** | **str** |  | [optional] 
**quotas** | [**list[NetworkQuota]**](NetworkQuota.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


