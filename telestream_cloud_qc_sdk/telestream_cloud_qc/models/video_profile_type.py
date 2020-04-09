# coding: utf-8

"""
    Qc API

    Qc API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_qc.configuration import Configuration


class VideoProfileType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    VIDEOPROFILENONE = "VideoProfileNone"
    H264BASELINE = "H264Baseline"
    H264MAIN = "H264Main"
    H264EXTENDED = "H264Extended"
    H264HIGH = "H264High"
    H264HIGH10 = "H264High10"
    H264HIGH422 = "H264High422"
    H264HIGH444 = "H264High444"
    H264HIGH10INTRA = "H264High10Intra"
    H264HIGH422INTRA = "H264High422Intra"
    H264HIGH444INTRA = "H264High444Intra"
    MPEG2SIMPLE = "Mpeg2Simple"
    MPEG2MAIN = "Mpeg2Main"
    MPEG2SNR = "Mpeg2Snr"
    MPEG2SPATIAL = "Mpeg2Spatial"
    MPEG2HIGH = "Mpeg2High"
    MPEG2422 = "Mpeg2422"
    MPEG2MVP = "Mpeg2Mvp"
    VC1SIMPLE = "Vc1Simple"
    VC1MAIN = "Vc1Main"
    VC1ADVANCED = "Vc1Advanced"
    PRORESNORMAL = "ProResNormal"
    PRORESHQ = "ProResHq"
    PRORESLT = "ProResLt"
    PRORESPROXY = "ProResProxy"
    PRORES4444 = "ProRes4444"
    HEVCMAIN = "HevcMain"
    HEVCMAIN10 = "HevcMain10"
    HEVCMAINSTILL = "HevcMainStill"
    PRORES4444XQ = "ProRes4444Xq"

    allowable_values = [VIDEOPROFILENONE, H264BASELINE, H264MAIN, H264EXTENDED, H264HIGH, H264HIGH10, H264HIGH422, H264HIGH444, H264HIGH10INTRA, H264HIGH422INTRA, H264HIGH444INTRA, MPEG2SIMPLE, MPEG2MAIN, MPEG2SNR, MPEG2SPATIAL, MPEG2HIGH, MPEG2422, MPEG2MVP, VC1SIMPLE, VC1MAIN, VC1ADVANCED, PRORESNORMAL, PRORESHQ, PRORESLT, PRORESPROXY, PRORES4444, HEVCMAIN, HEVCMAIN10, HEVCMAINSTILL, PRORES4444XQ]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """VideoProfileType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, VideoProfileType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VideoProfileType):
            return True

        return self.to_dict() != other.to_dict()
