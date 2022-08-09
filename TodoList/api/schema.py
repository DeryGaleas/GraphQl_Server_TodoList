from TodoList.api.query import Query
from TodoList.api.mutation import Mutation
from strawberry import Schema

schema = Schema(query=Query, mutation=Mutation )