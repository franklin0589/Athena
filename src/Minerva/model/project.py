import datetime as date
import peewee as p
from Minerva.model.base import BaseModel

class Project(BaseModel):
    name = p.CharField()
    description = p.TextField(null=True)
    task_count = p.IntegerField(default=0)
    created_at = p.DateTimeField(default=date.datetime.now)
    completed = p.BooleanField(default=False)
    updated_at = p.DateTimeField(default=date.datetime.now)
