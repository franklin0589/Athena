import os
import json
import sys
from pathlib import Path

def build_file(path:str):
    if not Path(path).exists():
        with open(path, "w") as f:
            ...

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def write_json(path, obj):
    with open(path, "w") as f:
        return json.dump(obj, f)

def exists(path):
    return Path(path).exists()

def make_folder(path):
    if not Path(path).exists():
        os.mkdir(path)

def get_directory(path:str):
    return os.path.dirname(path)

def join(pathA:str, pathB:str):
    return os.path.join(pathA, pathB)

def resource_path(relative_path:str) -> str:
    # If running as a PyInstaller EXE
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        # Running in normal Python
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)