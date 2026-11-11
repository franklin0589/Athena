import peewee as p
from Minerva.model.base import BaseModel
from Minerva.model.project import Project

class Task(BaseModel):
    name = p.CharField()
    description = p.TextField(null=True)
    project = p.ForeignKeyField(Project, backref='tasks')
    goal = p.CharField()
    finished = p.BooleanField(default=False)
    due_date = p.DateTimeField()
