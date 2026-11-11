import logging
import logging.handlers as h
import rich.logging as rL
from datetime import datetime

import Minerva.extern.file as fh

def get_logger(name:str, level = logging.INFO) -> logging.Logger:
    log_handle = logging.Logger(name)
    log_handle.setLevel(level)

    rich_handler = rL.RichHandler(level=level, tracebacks_show_locals=True)
    fmt = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    rich_handler.setFormatter(fmt)
    log_handle.addHandler(rich_handler)

    fh.make_folder(fh.resource_path("logs/"))


    date_str = datetime.now().strftime(f"%Y-%m-%d_%H-%M-%S_{name}")
    log_file = fh.resource_path(f"logs/{date_str}.log")
    file_handler = h.RotatingFileHandler(log_file)
    file_handler.doRollover()
    file_handler.setFormatter(fmt)
    log_handle.addHandler(file_handler)
    return log_handle


class LogManager:
    loggers = {}

    def get_logger(self, name:str, level = logging.INFO) -> logging.Logger:
        if name not in self.loggers:
            LogManager.loggers[name] = get_logger(name, level)
        return LogManager.loggers[name]

def view_logger() -> logging.Logger:
    logger = LogManager()
    return logger.get_logger("view", logging.INFO)

def error_logger() -> logging.Logger:
    logger = LogManager()
    return logger.get_logger("error", logging.ERROR)

def app_logger() -> logging.Logger:
    logger = LogManager()
    return logger.get_logger("app", logging.INFO)
    
def context_logger() -> logging.Logger:
    logger = LogManager()
    return logger.get_logger("context", logging.INFO)

if __name__ == "__main__":
    l = get_logger("Test", logging.DEBUG)
    for i in range(10):
        l.debug(f"Debug Message {i}")
        l.info(f"Info Message {i}")
        l.warning(f"Warning Message {i}")
        l.error(f"Error Message {i}")
        l.critical(f"Critical Message {i}")
    