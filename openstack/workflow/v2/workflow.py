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

from openstack import resource2 as resource
from openstack.workflow import workflow_service


class Workflow(resource.Resource):
    resource_key = 'workflow'
    resources_key = 'workflows'
    base_path = '/workflows'
    service = workflow_service.WorkflowService()

    # capabilities
    allow_create = True
    allow_list = True
    allow_get = True
    allow_delete = True

    marker = resource.Body("marker")
    limit = resource.Body("limit")
    sort_keys = resource.Body("sort_keys")
    sort_dirs = resource.Body("sort_dirs")
    fields = resource.Body("fields")
    name = resource.Body("name")
    input = resource.Body("input")
    definition = resource.Body("definition")
    tags = resource.Body("tags")
    scope = resource.Body("scope")
    project_id = resource.Body("project_id")
    created_at = resource.Body("created_at")
    updated_at = resource.Body("updated_at")

    def create(self, session, prepend_key=True):
        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)

        headers = {
            "Content-Type": 'text/plain'
        }
        uri=request.uri+"?scope=private"
        definition = request.body["workflow"]["definition"]
        request.headers.update(headers)
        response = session.post(uri, endpoint_filter=self.service,
                               json=None, definition, headers=request.headers)

        self._translate_response(response, has_body=False)
        return self
