from typing import List, Optional

from strawberry_django.filters import FilterLookup
from strawberry_django_plus import gql


@gql.interface(description=" It gives the API user a hint on the not allowed inputs or errors in the mutation.")
class TaskError:
    field: str
    message: str


@gql.interface()
class PayloadTypeInterface:
    task_errors: List[TaskError]
    node: Optional[gql.Node]


@gql.interface()
class InputTypeInterface:
    async def validate_and_get_error(self)-> List[TaskError]:
        pass

@gql.input()
class Filter:
    id:Optional[FilterLookup[gql.ID]]