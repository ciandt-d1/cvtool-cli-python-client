# coding: utf-8

"""
    Kingpick Admin API

    Provides APIs for tenant maintenance

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from cvtool_cli_client.models.tenants import Tenants


class TestTenants(unittest.TestCase):
    """ Tenants unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTenants(self):
        """
        Test Tenants
        """
        model = cvtool_cli_client.models.tenants.Tenants()


if __name__ == '__main__':
    unittest.main()
