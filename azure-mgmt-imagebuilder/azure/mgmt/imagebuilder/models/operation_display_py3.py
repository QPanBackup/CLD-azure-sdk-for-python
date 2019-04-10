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

from msrest.serialization import Model


class OperationDisplay(Model):
    """The object that describes the operation.

    :param provider: Friendly name of the resource provider.
    :type provider: str
    :param operation: The operation type. For example: read, write, delete, or
     listKeys/action
    :type operation: str
    :param resource: The resource type on which the operation is performed.
    :type resource: str
    :param description: The friendly name of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, operation: str=None, resource: str=None, description: str=None, **kwargs) -> None:
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.operation = operation
        self.resource = resource
        self.description = description
