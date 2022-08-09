from strawberry_django_plus import gql
from asgiref.sync import sync_to_async
from tasks.models import Task
from strawberry.types import Info
from.input import CreateTaskInput
from .types import TaskType
from .payload_types import CreateTaskPayload
from TodoList.api.utils.gql_mutation_payload import gql_mutation_payload

@gql.type
class Mutation:

    @gql_mutation_payload(
        input_type = CreateTaskInput,
        payload_type = CreateTaskPayload,
        returned_type= TaskType
    )
    async def create_task(self, input) -> TaskType:
        task = await sync_to_async(Task.objects.create)(
            name = input.name,
            description = input.description
        ) 
        return task