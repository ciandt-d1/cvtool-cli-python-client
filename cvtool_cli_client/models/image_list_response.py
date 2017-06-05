# coding: utf-8

"""
    Kingpick Admin API

    Provides APIs for tenant maintenance

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ImageListResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, meta=None, items=None):
        """
        ImageListResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'meta': 'MetaListResponse',
            'items': 'list[ImageResponse]'
        }

        self.attribute_map = {
            'meta': 'meta',
            'items': 'items'
        }

        self._meta = meta
        self._items = items

    @property
    def meta(self):
        """
        Gets the meta of this ImageListResponse.

        :return: The meta of this ImageListResponse.
        :rtype: MetaListResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this ImageListResponse.

        :param meta: The meta of this ImageListResponse.
        :type: MetaListResponse
        """

        self._meta = meta

    @property
    def items(self):
        """
        Gets the items of this ImageListResponse.

        :return: The items of this ImageListResponse.
        :rtype: list[ImageResponse]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ImageListResponse.

        :param items: The items of this ImageListResponse.
        :type: list[ImageResponse]
        """

        self._items = items

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
        if not isinstance(other, ImageListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other