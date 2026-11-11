from Minerva.Controllers.context import AppContext, PContext
from Minerva.model.project import Project

from Minerva.views.project import ProjectView
from typing import Optional

class ProjectController:
    def __init__(self):
        self.project:Optional[Project] = None
        self.view = ProjectView()

    def make(self, root_location:str, data:str):
        root_path = root_location
        if not self.view.verify(root_path, data):
            return
        
        self.project = Project(root_path, data)

    def add_task(self, data:str):
        if not self.verify_task(self.project, data):
            return 

        name, goal, duration, diff = data.split(",")

        self.view.show(name, goal, duration, diff)
        self.project.new_task(name, goal, int(duration), int(diff))

        self.view.save(self.project)
        self.project.save()


    def loop(self, app_context:PContext) -> int:
        res_key, data = app_context.console.cli_interface()
        if res_key == -1:
            return -1

        method = getattr(self, res_key, None)
        if method is None:
            app_context.console.print(f"[red]Error[/red] : Command {res_key} Not Found!")
        else:
            method(app_context, data)

        return 0    
