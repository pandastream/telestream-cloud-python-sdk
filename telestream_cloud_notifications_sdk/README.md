# Telestream Cloud Notifications Python SDK

This library provides a low-level interface to the REST API of Telestream Cloud, the online video encoding service.

## Requirements.

Python 2.7 and 3.4+

## Getting Started

## Documentation for API Endpoints

All URIs are relative to *https://api.cloud.telestream.net/notifications/v2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NotificationsApi* | [**create_subscription**](docs/NotificationsApi.md#create_subscription) | **POST** /subscriptions | Create a new subscription
*NotificationsApi* | [**delete_subscription**](docs/NotificationsApi.md#delete_subscription) | **DELETE** /subscriptions/{id} | 
*NotificationsApi* | [**get_subscription**](docs/NotificationsApi.md#get_subscription) | **GET** /subscriptions/{id} | 
*NotificationsApi* | [**list_subscriptions**](docs/NotificationsApi.md#list_subscriptions) | **GET** /subscriptions | 
*NotificationsApi* | [**modify_subscription**](docs/NotificationsApi.md#modify_subscription) | **PUT** /subscriptions/{id} | Modify subscription


## Documentation For Models

 - [Params](docs/Params.md)
 - [Subscription](docs/Subscription.md)
 - [Topic](docs/Topic.md)
 - [UpdateData](docs/UpdateData.md)
 - [UpdateTopic](docs/UpdateTopic.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header


## Author

cloudsupport@telestream.net


