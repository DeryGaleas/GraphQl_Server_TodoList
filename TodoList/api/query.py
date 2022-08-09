from strawberry_django_plus import gql
from tasks.api.query import Query as TaskQuery
@gql.type
class Query(TaskQuery):
    pass