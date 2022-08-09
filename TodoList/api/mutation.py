from strawberry_django_plus import gql
from tasks.api.mutation import Mutation as TaskMutation

@gql.type()
class Mutation(TaskMutation):
    pass
