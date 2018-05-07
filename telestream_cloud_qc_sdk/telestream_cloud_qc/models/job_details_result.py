# coding: utf-8

"""
    Qc API

    QC API  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_qc.models.alert import Alert  # noqa: F401,E501


class JobDetailsResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alerts': 'list[Alert]',
        'reports': 'list[str]'
    }

    attribute_map = {
        'alerts': 'alerts',
        'reports': 'reports'
    }

    def __init__(self, alerts=None, reports=None):  # noqa: E501
        """JobDetailsResult - a model defined in Swagger"""  # noqa: E501

        self._alerts = None
        self._reports = None
        self.discriminator = None

        if alerts is not None:
            self.alerts = alerts
        if reports is not None:
            self.reports = reports

    @property
    def alerts(self):
        """Gets the alerts of this JobDetailsResult.  # noqa: E501


        :return: The alerts of this JobDetailsResult.  # noqa: E501
        :rtype: list[Alert]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this JobDetailsResult.


        :param alerts: The alerts of this JobDetailsResult.  # noqa: E501
        :type: list[Alert]
        """

        self._alerts = alerts

    @property
    def reports(self):
        """Gets the reports of this JobDetailsResult.  # noqa: E501


        :return: The reports of this JobDetailsResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this JobDetailsResult.


        :param reports: The reports of this JobDetailsResult.  # noqa: E501
        :type: list[str]
        """

        self._reports = reports

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, JobDetailsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
