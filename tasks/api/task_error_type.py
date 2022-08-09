from strawberry_django_plus import gql

from TodoList.api.types import TaskError

@gql.type
class NameNotUnique(TaskError):
    message : str
    field : str

    @gql.django.field
    async def field(self) -> str:
        return "name"

        