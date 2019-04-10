# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class ImageTemplate(Resource):
    """ImageTemplate.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param source: Required. Specifies the properties used to describe the
     source image.
    :type source: ~azure.mgmt.imagebuilder.models.ImageTemplateSource
    :param customize: Specifies the properties used to describe the
     customization steps of the image, like Image source etc
    :type customize:
     list[~azure.mgmt.imagebuilder.models.ImageTemplateCustomizer]
    :param distribute: Required. The distribution targets where the image
     output needs to go to.
    :type distribute:
     list[~azure.mgmt.imagebuilder.models.ImageTemplateDistributor]
    :ivar provisioning_state: Provisioning state of the resource. Possible
     values include: 'Creating', 'Succeeded', 'Failed', 'Deleting'
    :vartype provisioning_state: str or ~azure.mgmt.imagebuilder.models.enum
    :ivar provisioning_error: Provisioning error, if any
    :vartype provisioning_error:
     ~azure.mgmt.imagebuilder.models.ProvisioningError
    :ivar last_run_status: State of 'run' that is currently executing or was
     last executed.
    :vartype last_run_status:
     ~azure.mgmt.imagebuilder.models.ImageTemplateLastRunStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'source': {'required': True},
        'distribute': {'required': True},
        'provisioning_state': {'readonly': True},
        'provisioning_error': {'readonly': True},
        'last_run_status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'source': {'key': 'properties.source', 'type': 'ImageTemplateSource'},
        'customize': {'key': 'properties.customize', 'type': '[ImageTemplateCustomizer]'},
        'distribute': {'key': 'properties.distribute', 'type': '[ImageTemplateDistributor]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'provisioning_error': {'key': 'properties.provisioningError', 'type': 'ProvisioningError'},
        'last_run_status': {'key': 'properties.lastRunStatus', 'type': 'ImageTemplateLastRunStatus'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplate, self).__init__(**kwargs)
        self.source = kwargs.get('source', None)
        self.customize = kwargs.get('customize', None)
        self.distribute = kwargs.get('distribute', None)
        self.provisioning_state = None
        self.provisioning_error = None
        self.last_run_status = None
