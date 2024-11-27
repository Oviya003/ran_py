# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.31
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1LinuxContainerUser(object):
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
        'gid': 'int',
        'supplemental_groups': 'list[int]',
        'uid': 'int'
    }

    attribute_map = {
        'gid': 'gid',
        'supplemental_groups': 'supplementalGroups',
        'uid': 'uid'
    }

    def __init__(self, gid=None, supplemental_groups=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """V1LinuxContainerUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gid = None
        self._supplemental_groups = None
        self._uid = None
        self.discriminator = None

        self.gid = gid
        if supplemental_groups is not None:
            self.supplemental_groups = supplemental_groups
        self.uid = uid

    @property
    def gid(self):
        """Gets the gid of this V1LinuxContainerUser.  # noqa: E501

        GID is the primary gid initially attached to the first process in the container  # noqa: E501

        :return: The gid of this V1LinuxContainerUser.  # noqa: E501
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this V1LinuxContainerUser.

        GID is the primary gid initially attached to the first process in the container  # noqa: E501

        :param gid: The gid of this V1LinuxContainerUser.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and gid is None:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must not be `None`")  # noqa: E501

        self._gid = gid

    @property
    def supplemental_groups(self):
        """Gets the supplemental_groups of this V1LinuxContainerUser.  # noqa: E501

        SupplementalGroups are the supplemental groups initially attached to the first process in the container  # noqa: E501

        :return: The supplemental_groups of this V1LinuxContainerUser.  # noqa: E501
        :rtype: list[int]
        """
        return self._supplemental_groups

    @supplemental_groups.setter
    def supplemental_groups(self, supplemental_groups):
        """Sets the supplemental_groups of this V1LinuxContainerUser.

        SupplementalGroups are the supplemental groups initially attached to the first process in the container  # noqa: E501

        :param supplemental_groups: The supplemental_groups of this V1LinuxContainerUser.  # noqa: E501
        :type: list[int]
        """

        self._supplemental_groups = supplemental_groups

    @property
    def uid(self):
        """Gets the uid of this V1LinuxContainerUser.  # noqa: E501

        UID is the primary uid initially attached to the first process in the container  # noqa: E501

        :return: The uid of this V1LinuxContainerUser.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1LinuxContainerUser.

        UID is the primary uid initially attached to the first process in the container  # noqa: E501

        :param uid: The uid of this V1LinuxContainerUser.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

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
        if not isinstance(other, V1LinuxContainerUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1LinuxContainerUser):
            return True

        return self.to_dict() != other.to_dict()
