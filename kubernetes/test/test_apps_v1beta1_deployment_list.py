# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.apps_v1beta1_deployment_list import AppsV1beta1DeploymentList


class TestAppsV1beta1DeploymentList(unittest.TestCase):
    """ AppsV1beta1DeploymentList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAppsV1beta1DeploymentList(self):
        """
        Test AppsV1beta1DeploymentList
        """
        model = kubernetes.client.models.apps_v1beta1_deployment_list.AppsV1beta1DeploymentList()


if __name__ == '__main__':
    unittest.main()