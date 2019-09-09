from . import db
from typing import List
from src.modules.executor import Executor


def update_executors(names: List[str]):
    for name in names:
        executor = Executor(name=name)
