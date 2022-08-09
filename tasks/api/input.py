from strawberry_django_plus import gql
from tasks.models import Task
from strawberry import auto
from typing import List
from TodoList.api.types import InputTypeInterface, TaskError
from tasks.api.task_error_type import NameNotUnique
from asgiref.sync import sync_to_async


@gql.django.input(Task)
class CreateTaskInput(InputTypeInterface):
    name: auto
    description: auto

    async def validate_and_get_errors(self) -> List[TaskError]:
        errors = []
        if await sync_to_async(Task.objects.filter(name=self.name).exists)():
            errors.append(
                NameNotUnique(
                    message="Name is not unique"
                )
            )
        return errors
