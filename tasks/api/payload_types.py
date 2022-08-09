from strawberry_django_plus import gql
from typing import List, Optional
from tasks.api.types import TaskType 
from TodoList.api.types import PayloadTypeInterface, TaskError


@gql.type
class CreateTaskPayload(PayloadTypeInterface):
    node: Optional[TaskType]
    task_errors: List[TaskError]

  