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
from openstack.workflow.v2 import task as _task
from openstack.workflow.v2 import action as _action
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

    def create_execution(self, workflow_name, **attrs):
        """Create a new execution from attributes

        :param workflow_name: The name of target workflow to execution workflow from.
        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~openstack.workflow.v2.execution.Execution`,
            comprised of the properties on the Execution class.

        :returns: The results of execution creation
        :rtype: :class:`~openstack.workflow.v2.execution.Execution`
        """
        return self._create(_execution.Execution, workflow_name=workflow_name, **attrs)

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
        return self._list(_workflow.Execution, paginated=True, **query)

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

    def create_task(self, workflow_name, **attrs):
        """Create a new task from attributes

        :param workflow_name: The name of target queue to subscribe on.
        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~openstack.message.v2.task.Task`,
            comprised of the properties on the Task class.

        :returns: The results of task creation
        :rtype: :class:`~openstack.message.v2.task.Task`
        """
        return self._create(_task.Task, workflow_name=workflow_name,
                            **attrs)

    def tasks(self, workflow_name, **query):
        """Retrieve a generator of tasks

        :param workflow_name: The name of target queue to subscribe on.
        :param kwargs \*\*query: Optional query parameters to be sent to
            restrict the tasks to be returned. Available parameters
            include:

            * limit: Requests at most the specified number of items be
                returned from the query.
            * marker: Specifies the ID of the last-seen task. Use the
                limit parameter to make an initial limited request and use the
                ID of the last-seen task from the response as the
                marker parameter value in a subsequent limited request.

        :returns: A generator of task instances.
        """
        query["workflow_name"] = workflow_name
        return self._list(_task.Task, paginated=True, **query)

    def get_task(self, workflow_name, task):
        """Get a task

        :param workflow_name: The name of target queue of task.
        :param message: The value can be the ID of a task or a
            :class:`~openstack.message.v2.task.Task` instance.

        :returns: One :class:`~openstack.message.v2.task.Task`
        :raises: :class:`~openstack.exceptions.ResourceNotFound` when no
            task matching the criteria could be found.
        """
        task = self._get_resource(_task.Task,
                                          task,
                                          workflow_name=workflow_name)
        return self._get(_task.Task, task)

    def delete_task(self, workflow_name, value, ignore_missing=True):
        """Delete a task

        :param workflow_name: The name of target queue to delete task
                           from.
        :param value: The value can be either the name of a task or a
                      :class:`~openstack.message.v2.task.Task`
                      instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the task does not exist.
                    When set to ``True``, no exception will be thrown when
                    attempting to delete a nonexistent task.

        :returns: ``None``
        """
        task = self._get_resource(_task.Task, value,
                                          workflow_name=workflow_name)
        return self._delete(_task.Task, task,
                            ignore_missing=ignore_missing)

    def create_action(self, workflow_name, **attrs):
        """Create a new action from attributes

        :param workflow_name: The name of target queue to action message from.
        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~openstack.message.v2.action.Action`,
            comprised of the properties on the Action class.

        :returns: The results of action creation
        :rtype: :class:`~openstack.message.v2.action.Action`
        """
        return self._create(_action.Action, workflow_name=workflow_name, **attrs)

    def get_action(self, workflow_name, action):
        """Get a action

        :param workflow_name: The name of target queue to action message from.
        :param action: The value can be either the ID of a action or a
            :class:`~openstack.message.v2.action.Action` instance.

        :returns: One :class:`~openstack.message.v2.action.Action`
        :raises: :class:`~openstack.exceptions.ResourceNotFound` when no
            action matching the criteria could be found.
        """
        return self._get(_action.Action, action, workflow_name=workflow_name)

    def update_action(self, workflow_name, action, **attrs):
        """Update an existing action from attributes

        :param workflow_name: The name of target queue to action message from.
        :param action: The value can be either the ID of a action or a
            :class:`~openstack.message.v2.action.Action` instance.
        :param dict attrs: Keyword arguments which will be used to update a
            :class:`~openstack.message.v2.action.Action`,
            comprised of the properties on the Action class.

        :returns: The results of action update
        :rtype: :class:`~openstack.message.v2.action.Action`
        """
        return self._update(_action.Action, action, workflow_name=workflow_name,
                            **attrs)

    def delete_action(self, workflow_name, action, ignore_missing=True):
        """Delete a action

        :param workflow_name: The name of target queue to action messages from.
        :param action: The value can be either the ID of a action or a
                      :class:`~openstack.message.v2.action.Action` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the action does not exist.
                    When set to ``True``, no exception will be thrown when
                    attempting to delete a nonexistent action.

        :returns: ``None``
        """
        return self._delete(_action.Action, action, workflow_name=workflow_name,
                            ignore_missing=ignore_missing)
