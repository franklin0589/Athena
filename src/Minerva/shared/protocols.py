from typing import Protocol

class PAppConfig(Protocol):
    ...

class PConsole(Protocol):
    ...

class PContext(Protocol):
    config  : PAppConfig
    console : PConsole


class Command(Protocol):
    decription:str

    def check(self, app, data): ...
    def run(self, app, data): ...
    def __call__(self, app, data): ...