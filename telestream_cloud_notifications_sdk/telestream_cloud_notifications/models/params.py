# coding: utf-8

"""
    Notifications API

    Notifications  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_notifications.configuration import Configuration


class Params(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'addresses': 'list[str]',
        'url': 'str',
        'method': 'str',
        'retries': 'int',
        'content_type': 'str',
        'topic_arn': 'str',
        'role_arn': 'str',
        'topic_endpoint': 'str',
        'access_key': 'str',
        'project_id': 'str',
        'topic_name': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'url': 'url',
        'method': 'method',
        'retries': 'retries',
        'content_type': 'content_type',
        'topic_arn': 'topic_arn',
        'role_arn': 'role_arn',
        'topic_endpoint': 'topic_endpoint',
        'access_key': 'access_key',
        'project_id': 'project_id',
        'topic_name': 'topic_name'
    }

    def __init__(self, addresses=None, url=None, method=None, retries=None, content_type=None, topic_arn=None, role_arn=None, topic_endpoint=None, access_key=None, project_id=None, topic_name=None, local_vars_configuration=None):  # noqa: E501
        """Params - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._url = None
        self._method = None
        self._retries = None
        self._content_type = None
        self._topic_arn = None
        self._role_arn = None
        self._topic_endpoint = None
        self._access_key = None
        self._project_id = None
        self._topic_name = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if url is not None:
            self.url = url
        if method is not None:
            self.method = method
        if retries is not None:
            self.retries = retries
        if content_type is not None:
            self.content_type = content_type
        if topic_arn is not None:
            self.topic_arn = topic_arn
        if role_arn is not None:
            self.role_arn = role_arn
        if topic_endpoint is not None:
            self.topic_endpoint = topic_endpoint
        if access_key is not None:
            self.access_key = access_key
        if project_id is not None:
            self.project_id = project_id
        if topic_name is not None:
            self.topic_name = topic_name

    @property
    def addresses(self):
        """Gets the addresses of this Params.  # noqa: E501

        (for email subscription type);  E-mail addresses   # noqa: E501

        :return: The addresses of this Params.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Params.

        (for email subscription type);  E-mail addresses   # noqa: E501

        :param addresses: The addresses of this Params.  # noqa: E501
        :type: list[str]
        """

        self._addresses = addresses

    @property
    def url(self):
        """Gets the url of this Params.  # noqa: E501

        (for webhook subscription type);  Webhook URL   # noqa: E501

        :return: The url of this Params.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Params.

        (for webhook subscription type);  Webhook URL   # noqa: E501

        :param url: The url of this Params.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def method(self):
        """Gets the method of this Params.  # noqa: E501

        (for webhook subscription type);  HTTP method; default: POST (GET, POST)   # noqa: E501

        :return: The method of this Params.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Params.

        (for webhook subscription type);  HTTP method; default: POST (GET, POST)   # noqa: E501

        :param method: The method of this Params.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "POST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def retries(self):
        """Gets the retries of this Params.  # noqa: E501

        (for webhook subscription type);  Number of retries before forgetting the notification; default: 0   # noqa: E501

        :return: The retries of this Params.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this Params.

        (for webhook subscription type);  Number of retries before forgetting the notification; default: 0   # noqa: E501

        :param retries: The retries of this Params.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def content_type(self):
        """Gets the content_type of this Params.  # noqa: E501

        (for webhook subscription type); default: application/json (application/json, application/x-www-form-urlencoded)   # noqa: E501

        :return: The content_type of this Params.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Params.

        (for webhook subscription type); default: application/json (application/json, application/x-www-form-urlencoded)   # noqa: E501

        :param content_type: The content_type of this Params.  # noqa: E501
        :type: str
        """
        allowed_values = ["application/json", "application/x-www-form-urlencoded"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and content_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def topic_arn(self):
        """Gets the topic_arn of this Params.  # noqa: E501

        (for sns subscription type) identifier of an AWS SNS Topic that events will be posted to.   # noqa: E501

        :return: The topic_arn of this Params.  # noqa: E501
        :rtype: str
        """
        return self._topic_arn

    @topic_arn.setter
    def topic_arn(self, topic_arn):
        """Sets the topic_arn of this Params.

        (for sns subscription type) identifier of an AWS SNS Topic that events will be posted to.   # noqa: E501

        :param topic_arn: The topic_arn of this Params.  # noqa: E501
        :type: str
        """

        self._topic_arn = topic_arn

    @property
    def role_arn(self):
        """Gets the role_arn of this Params.  # noqa: E501

        (for sns subscription type) identifier of an AWS IAM Role that will be used for authorization.   # noqa: E501

        :return: The role_arn of this Params.  # noqa: E501
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this Params.

        (for sns subscription type) identifier of an AWS IAM Role that will be used for authorization.   # noqa: E501

        :param role_arn: The role_arn of this Params.  # noqa: E501
        :type: str
        """

        self._role_arn = role_arn

    @property
    def topic_endpoint(self):
        """Gets the topic_endpoint of this Params.  # noqa: E501

        (for aeg subscription type) address of an Azure Event Grid Topic that events will be posted to.   # noqa: E501

        :return: The topic_endpoint of this Params.  # noqa: E501
        :rtype: str
        """
        return self._topic_endpoint

    @topic_endpoint.setter
    def topic_endpoint(self, topic_endpoint):
        """Sets the topic_endpoint of this Params.

        (for aeg subscription type) address of an Azure Event Grid Topic that events will be posted to.   # noqa: E501

        :param topic_endpoint: The topic_endpoint of this Params.  # noqa: E501
        :type: str
        """

        self._topic_endpoint = topic_endpoint

    @property
    def access_key(self):
        """Gets the access_key of this Params.  # noqa: E501

        (for aeg subscription type) secret access key that authorizes Telestream Cloud to write to an Azure Event Grid Topic.   # noqa: E501

        :return: The access_key of this Params.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this Params.

        (for aeg subscription type) secret access key that authorizes Telestream Cloud to write to an Azure Event Grid Topic.   # noqa: E501

        :param access_key: The access_key of this Params.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def project_id(self):
        """Gets the project_id of this Params.  # noqa: E501

        (for pubsub subscription type) id of a Google Cloud project that hosts the topic.   # noqa: E501

        :return: The project_id of this Params.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Params.

        (for pubsub subscription type) id of a Google Cloud project that hosts the topic.   # noqa: E501

        :param project_id: The project_id of this Params.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def topic_name(self):
        """Gets the topic_name of this Params.  # noqa: E501

        (for pubsub subscription type) name of a Google Cloud Pub/Sub topic to which notifications will be published.   # noqa: E501

        :return: The topic_name of this Params.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this Params.

        (for pubsub subscription type) name of a Google Cloud Pub/Sub topic to which notifications will be published.   # noqa: E501

        :param topic_name: The topic_name of this Params.  # noqa: E501
        :type: str
        """

        self._topic_name = topic_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Params):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Params):
            return True

        return self.to_dict() != other.to_dict()
