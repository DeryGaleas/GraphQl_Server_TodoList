from strawberry_django_plus import gql
from strawberry.types import Info
from .types import TaskType
from .utils import convert_query_set_to_async_list
from tasks.models import Task
from typing import List


@gql.type()

class Query:

    @gql.django.field
    async def tasks_done(self, info:Info) -> List[TaskType]:
        tasks = await convert_query_set_to_async_list(Task.objects.filter(is_done = False))
        return tasks

    @gql.connection
    async def tasks_connection(self)-> gql.Connection[TaskType]:
        task_list = convert_query_set_to_async_list(Task.objects.filter(is_done =False))
        return task_list




