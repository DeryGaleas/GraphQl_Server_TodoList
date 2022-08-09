from tasks.models import Task
from strawberry_django_plus import gql
from strawberry import auto
from strawberry_django_plus.gql import relay

@gql.django.type(Task)
class TaskType(relay.Node):
    id : auto
    name : auto
    description : auto
    is_done : auto


