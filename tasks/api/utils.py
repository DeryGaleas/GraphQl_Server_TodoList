from asgiref.sync import sync_to_async
from django.db.models import QuerySet
from typing import List




async def convert_query_set_to_async_list(query_set: QuerySet) -> List:
    async_list = sync_to_async(list) 
    return await async_list(query_set)
    