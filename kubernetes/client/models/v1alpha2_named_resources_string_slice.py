# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.30
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha2NamedResourcesStringSlice(object):
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
        'strings': 'list[str]'
    }

    attribute_map = {
        'strings': 'strings'
    }

    def __init__(self, strings=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2NamedResourcesStringSlice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._strings = None
        self.discriminator = None

        self.strings = strings

    @property
    def strings(self):
        """Gets the strings of this V1alpha2NamedResourcesStringSlice.  # noqa: E501

        Strings is the slice of strings.  # noqa: E501

        :return: The strings of this V1alpha2NamedResourcesStringSlice.  # noqa: E501
        :rtype: list[str]
        """
        return self._strings

    @strings.setter
    def strings(self, strings):
        """Sets the strings of this V1alpha2NamedResourcesStringSlice.

        Strings is the slice of strings.  # noqa: E501

        :param strings: The strings of this V1alpha2NamedResourcesStringSlice.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and strings is None:  # noqa: E501
            raise ValueError("Invalid value for `strings`, must not be `None`")  # noqa: E501

        self._strings = strings

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
        if not isinstance(other, V1alpha2NamedResourcesStringSlice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2NamedResourcesStringSlice):
            return True

        return self.to_dict() != other.to_dict()