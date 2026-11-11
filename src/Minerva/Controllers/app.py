from Minerva.Controllers.context import AppContext

class MinervaApp:
    def __init__(self):
        self.controller = ProjectController()
        self.context = AppContext()

    def execute (self):
        while True:
            if self.controller.loop(self.context) == -1:
                break


if __name__ == "__main__":
    app = MinervaApp()
    app.execute()