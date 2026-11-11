
from Minerva.extern.appConfig import AppConfig
from typing import Protocol
from Minerva.views import *

class AppContext():
    def __init__(self):
        self.console = MinervaConsole()
        self.config = AppConfig()
    