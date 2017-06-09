# coding: utf-8

"""
    CVTool CLI API

    Provides APIs for tenant maintenance

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.annotations import Annotations
from .models.error import Error
from .models.image_list_response import ImageListResponse
from .models.image_request import ImageRequest
from .models.image_response import ImageResponse
from .models.job import Job
from .models.job_input_parameters import JobInputParameters
from .models.job_step import JobStep
from .models.meta_list_response import MetaListResponse
from .models.new_job_request import NewJobRequest
from .models.project import Project
from .models.projects import Projects
from .models.settings import Settings
from .models.tenant import Tenant
from .models.tenants import Tenants
from .models.vision_annotations import VisionAnnotations

# import apis into sdk package
from .apis.auth_api import AuthApi
from .apis.image_api import ImageApi
from .apis.job_api import JobApi
from .apis.project_api import ProjectApi
from .apis.tenant_api import TenantApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
