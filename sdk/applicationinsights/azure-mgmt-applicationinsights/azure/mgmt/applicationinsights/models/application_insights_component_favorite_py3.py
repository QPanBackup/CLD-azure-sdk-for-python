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


class ApplicationInsightsComponentFavorite(Model):
    """Properties that define a favorite that is associated to an Application
    Insights component.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The user-defined name of the favorite.
    :type name: str
    :param config: Configuration of this particular favorite, which are driven
     by the Azure portal UX. Configuration data is a string containing valid
     JSON
    :type config: str
    :param version: This instance's version of the data model. This can change
     as new features are added that can be marked favorite. Current examples
     include MetricsExplorer (ME) and Search.
    :type version: str
    :ivar favorite_id: Internally assigned unique id of the favorite
     definition.
    :vartype favorite_id: str
    :param favorite_type: Enum indicating if this favorite definition is owned
     by a specific user or is shared between all users with access to the
     Application Insights component. Possible values include: 'shared', 'user'
    :type favorite_type: str or
     ~azure.mgmt.applicationinsights.models.FavoriteType
    :param source_type: The source of the favorite definition.
    :type source_type: str
    :ivar time_modified: Date and time in UTC of the last modification that
     was made to this favorite definition.
    :vartype time_modified: str
    :param tags: A list of 0 or more tags that are associated with this
     favorite definition
    :type tags: list[str]
    :param category: Favorite category, as defined by the user at creation
     time.
    :type category: str
    :param is_generated_from_template: Flag denoting wether or not this
     favorite was generated from a template.
    :type is_generated_from_template: bool
    :ivar user_id: Unique user id of the specific user that owns this
     favorite.
    :vartype user_id: str
    """

    _validation = {
        'favorite_id': {'readonly': True},
        'time_modified': {'readonly': True},
        'user_id': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'config': {'key': 'Config', 'type': 'str'},
        'version': {'key': 'Version', 'type': 'str'},
        'favorite_id': {'key': 'FavoriteId', 'type': 'str'},
        'favorite_type': {'key': 'FavoriteType', 'type': 'FavoriteType'},
        'source_type': {'key': 'SourceType', 'type': 'str'},
        'time_modified': {'key': 'TimeModified', 'type': 'str'},
        'tags': {'key': 'Tags', 'type': '[str]'},
        'category': {'key': 'Category', 'type': 'str'},
        'is_generated_from_template': {'key': 'IsGeneratedFromTemplate', 'type': 'bool'},
        'user_id': {'key': 'UserId', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, config: str=None, version: str=None, favorite_type=None, source_type: str=None, tags=None, category: str=None, is_generated_from_template: bool=None, **kwargs) -> None:
        super(ApplicationInsightsComponentFavorite, self).__init__(**kwargs)
        self.name = name
        self.config = config
        self.version = version
        self.favorite_id = None
        self.favorite_type = favorite_type
        self.source_type = source_type
        self.time_modified = None
        self.tags = tags
        self.category = category
        self.is_generated_from_template = is_generated_from_template
        self.user_id = None