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

from openstack.workflow.v2 import workflow as _workflow
from openstack.workflow.v2 import execution as _execution
from openstack import proxy2
from openstack import resource2


class Proxy(proxy2.BaseProxy):

    def create_workflow(self, **attrs):
        """Create a new workflow from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.workflow.v2.workflow.Workflow`,
                           comprised of the properties on the Workflow class.

        :returns: The results of workflow creation
        :rtype: :class:`~openstack.workflow.v2.workflow.Workflow`
        """
        return self._create(_workflow.Workflow, **attrs)

    def get_workflow(self, workflow):
        """Get a workflow

        :param workflow: The value can be the name of a workflow or a
            :class:`~openstack.workflow.v2.workflow.Workflow` instance.

        :returns: One :class:`~openstack.workflow.v2.workflow.Workflow`
        :raises: :class:`~openstack.exceptions.ResourceNotFound` when no
            workflow matching the name could be found.
        """
        return self._get(_workflow.Workflow, workflow)

    def workflows(self, **query):
        """Retrieve a generator of workflows

        :param kwargs \*\*query: Optional query parameters to be sent to
            restrict the workflows to be returned. Available parameters include:

            * limit: Requests at most the specified number of items be
                returned from the query.
            * marker: Specifies the ID of the last-seen workflow. Use the limit
                parameter to make an initial limited request and use the ID of
                the last-seen workflow from the response as the marker parameter
                value in a subsequent limited request.

        :returns: A generator of workflow instances.
        """
        return self._list(_workflow.Workflow, paginated=True, **query)

    def delete_workflow(self, workflow_name, ignore_missing=True):
        """Delete a workflow

        :param value: The value can be either the name of a workflow or a
                      :class:`~openstack.workflow.v2.workflow.Workflow` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the workflow does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent workflow.

        :returns: ``None``
        """
        return self._delete(_workflow.Workflow, workflow_name, ignore_missing=ignore_missing)

    def create_execution(self, **attrs):
        """Create a new execution from attributes

        :param workflow_name: The name of target workflow to execution workflow from.
        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~openstack.workflow.v2.execution.Execution`,
            comprised of the properties on the Execution class.

        :returns: The results of execution creation
        :rtype: :class:`~openstack.workflow.v2.execution.Execution`
        """
        return self._create(_execution.Execution, **attrs)

    def get_execution(self, workflow_name, execution):
        """Get a execution

        :param workflow_name: The name of target workflow to execution workflow from.
        :param execution: The value can be either the ID of a execution or a
            :class:`~openstack.workflow.v2.execution.Execution` instance.

        :returns: One :class:`~openstack.workflow.v2.execution.Execution`
        :raises: :class:`~openstack.exceptions.ResourceNotFound` when no
            execution matching the criteria could be found.
        """
        return self._get(_execution.Execution, execution, workflow_name=workflow_name)

    def update_execution(self, workflow_name, execution, **attrs):
        """Update an existing execution from attributes

        :param workflow_name: The name of target workflow to execution workflow from.
        :param execution: The value can be either the ID of a execution or a
            :class:`~openstack.workflow.v2.execution.Execution` instance.
        :param dict attrs: Keyword arguments which will be used to update a
            :class:`~openstack.workflow.v2.execution.Execution`,
            comprised of the properties on the Execution class.

        :returns: The results of execution update
        :rtype: :class:`~openstack.workflow.v2.execution.Execution`
        """
        return self._update(_execution.Execution, execution, workflow_name=workflow_name,
                            **attrs)

    def executions(self, **query):
        """Retrieve a generator of workflows

        :param kwargs \*\*query: Optional query parameters to be sent to
            restrict the workflows to be returned. Available parameters include:

            * limit: Requests at most the specified number of items be
                returned from the query.
            * marker: Specifies the ID of the last-seen workflow. Use the limit
                parameter to make an initial limited request and use the ID of
                the last-seen workflow from the response as the marker parameter
                value in a subsequent limited request.

        :returns: A generator of workflow instances.
        """
        return self._list(_execution.Execution, paginated=True, **query)

    def delete_execution(self, workflow_name, execution, ignore_missing=True):
        """Delete a execution

        :param workflow_name: The name of target workflow to execution workflows from.
        :param execution: The value can be either the ID of a execution or a
                      :class:`~openstack.workflow.v2.execution.Execution` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the execution does not exist.
                    When set to ``True``, no exception will be thrown when
                    attempting to delete a nonexistent execution.

        :returns: ``None``
        """
        return self._delete(_execution.Execution, execution, workflow_name=workflow_name,
                            ignore_missing=ignore_missing)
