from abc import ABC, abstractmethod
from ..extern.appConfig import TaskStatus

class Command(ABC):
    def __init__(self):
        self.desc = ""
        self.buffer = []

    def split_data(self, app, data: str, req_len: int, sep=" ", maxsplit=-1):
        if data is None or not isinstance(data, str):
            app.print("Need to data to execute command")
            return None
        temp = data.split(sep=sep, maxsplit=maxsplit)
        if len(temp) != req_len:
            app.print( "Wrong Number of parameters for this command")
            return None
        return temp

    def check(self, app, data):
        return True

    @abstractmethod
    def run(self, app, data):

        ...

    def __call__(self, app, data):
        if self.check(app, data):
            self.run(app, data)


class AddStepCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Add a new step- add [italics] step[/italics]"

    def check(self, app, data):
        if not app.tm.is_task_selected():
            app.print(
                "Need to load a project before running the Add New Step Command")
            return False
        return True

    def run(self, app, data):
        app.tm.new_step(data)
        app.pm.append_step(data)


class ClearCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Clear the console"

    def run(self, app, data):
        app.pages[app.page_index].cmd_widget.reset()


class CloseCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Clear the console"

    def run(self, app, data):
        app.tm.remove()
        app.brd_display.h_task = "malefecence"
        app.input_dict = app.brd_command


class MoveCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Move a task somewhere else - drop [italics]CurrStatus CurrIndex NewStatus[/italics]"

    def check(self, app, data):
        if not app.pm.is_project_loaded():
            app.print("Need to load a project before show")
            return False

        res = self.split_data(app, data, 3)
        if res is None:
            return False
        if not res[0].isnumeric() or not res[1].isnumeric():
            app.print("Invalid Index Provided")
            return False
        self.buffer = res
        return True

    def run(self, app, data):
        status, index, dest_status = self.buffer
        app.km.move(int(status), int(index), int(dest_status))


class HelpCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Print all available the commands w/ descriptions"

    def run(self, app, data):
        for key in app.input_dict:
            comm = app.input_dict[key]
            app.print(f"[bold]\t {key}[/bold] \t - {comm.desc}")



class LoadCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Load a project - load [italics]ProjIndex [/italics]"

    def check(self, app, data):
        if data is None:
            app.print(
                "Need to provide a Project Index to Load Project")
            return False

        if not data.isnumeric() or int(data) < 0:
            app.print(
                f"Invalid Load Index provided. {data}.Please try again.")
            return False
        return True

    def run(self, app, data):
        if app.pm.is_project_loaded():
            app.print("Saving Existing Project...")
            app.pm.save()
        index = int(data)
        app.pm.load_project(index)
        app.page_index = 1

class MakeCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Make a New Task Board - make [italics]Name[/italics]"

    def run(self, app, data):
        name = data
        app.pm.make_project(name)


class SmartPushCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Push a task to next position - push [italics]CurrStatus CurrIndex[/italics]"

    def check(self, app, data):
        if not app.pm.is_project_loaded():
            app.print("Need to load a project before show")
            return False
        res = self.split_data(app, data, 1)
        if res == None:
            return False
        self.buffer = res
        return True

    def run(self, app, data):
        key = self.buffer[0]
        app.km.smart_push(key)


class ProgCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Progress to the next available step - prog "

    def check(self, app, data):
        if not app.pm.is_project_loaded():
            app.print("Need to load a project before show")
            return False
        if not app.tm.is_task_selected():
            return False
        return True

    def run(self, app, data):
        prog_value = int(data) if data is not None and data.isnumeric() else 33
        app.tm.progress(prog_value)


class NewCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Make a New Task - new [italics]Name Description[/italics]"

    def check(self, app, data):
        if not app.pm.is_project_loaded():
            app.print("Need to load a project before show")
            return False
        res = self.split_data(app, data, 2 , " ", 1)
        if res is None:
            return False
        self.buffer = res
        return True
    
    def run(self, app, data):
        name, description = self.buffer
        app.pm.new_task(name, description)


class ReviewCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Review - Select a task from Test and verify it is finished - review [italics] index [/italics] "
        self.status = 3

    def check(self, app, data):
        if not app.pm.is_project_loaded():
            app.print("Need to load a project before show")
            return False
        return True

    def run(self, app, data):

        index = int(data.strip())

        app.tm.move_task(2, index)

        for line in app.tm.describe(self.status, index):
            app.console.print(line)

        resp = app.console.input("Has this task been completed? (Y/N)")
        if resp.lower()[0] == "y":
            app.tm.move_task(3, -1)


class OpenCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Open the Task Display with current steps"
        
    def check(self, app, data):
        if not app.pm.is_project_loaded():
            app.print("Need to load a project before show")
            return False
        res = self.split_data(app, data, 2)
        if res == None:
            return False
        self.buffer = res
        return True

    def run(self, app, data):
        status, index = self.buffer
        task = app.km.get_task(int(status), int(index))
        app.tm.select(task)
        app.input_dict = app.tsk_command


class UrgentCommand(Command):
    def __init__(self):
        super().__init__()
        self.desc = "Create a new task and immediatele move it to the urgent position- urgent [italics]task description[/italics]"

    def check(self, app, data):
        if not app.pm.is_project_loaded():
            app.print("Need to load a project before show")
            return False
        res = self.split_data(app, data, 2, " ", 1)
        if res == None:
            return False
        self.buffer = res
        return True

    def run(self, app, data):
        name, description = self.buffer
        app.pm.new_task(name, description, TaskStatus.working)

