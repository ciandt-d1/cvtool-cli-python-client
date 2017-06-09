# coding: utf-8

"""
    CVTool CLI API

    Provides APIs for tenant maintenance

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Tenant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, description=None, settings=None):
        """
        Tenant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'settings': 'Settings'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'settings': 'settings'
        }

        self._id = id
        self._name = name
        self._description = description
        self._settings = settings

    @property
    def id(self):
        """
        Gets the id of this Tenant.

        :return: The id of this Tenant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tenant.

        :param id: The id of this Tenant.
        :type: str
        """
        if id is not None and len(id) > 64:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `64`")
        if id is not None and len(id) < 3:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `3`")
        if id is not None and not re.search('[a-z0-9-_\\.]{3,64}', id):
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/[a-z0-9-_\\.]{3,64}/`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Tenant.

        :return: The name of this Tenant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tenant.

        :param name: The name of this Tenant.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Tenant.

        :return: The description of this Tenant.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Tenant.

        :param description: The description of this Tenant.
        :type: str
        """

        self._description = description

    @property
    def settings(self):
        """
        Gets the settings of this Tenant.

        :return: The settings of this Tenant.
        :rtype: Settings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this Tenant.

        :param settings: The settings of this Tenant.
        :type: Settings
        """

        self._settings = settings

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Tenant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
