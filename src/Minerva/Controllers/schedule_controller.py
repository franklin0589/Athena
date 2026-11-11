from Minerva.Controllers.context import AppContext, PContext
from Minerva.controller.base import AppController

class ScheduleController(AppController):
    def __init__(self):
        self.schedule = None

    def loop(self, context:PContext) -> int:
        ...