from django.db import models

class Task(models.Model): 
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=60)
    is_done = models.BooleanField(default=False)



