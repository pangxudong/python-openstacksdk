# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import uuid

from openstack.workflow import workflow_service
from openstack import resource2


class Action(resource2.Resource):
    resource_key = 'action'
    resources_key = 'actions'
    base_path = '/actions'
    service = workflow_service.WorkflowService()

    # capabilities
    allow_create = True
    allow_list = True
    allow_get = True
    allow_delete = True

    marker = resource2.Body("marker")
    limit = resource2.Body("limit")
    sort_keys = resource2.Body("sort_keys")
    sort_dirs = resource2.Body("sort_dirs")
    fields = resource2.Body("fields")
    name = resource2.Body("name")
    scope = resource2.Body("scope")
    definition = resource2.Body("definition")
    is_system = resource2.Body("is_system")
    input = resource2.Body("input")
    description = resource2.Body("description")
    tags = resource2.Body("tags")
    created_at = resource2.Body("created_at")
    updated_at = resource2.Body("updated_at")
