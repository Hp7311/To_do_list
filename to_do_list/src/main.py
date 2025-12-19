"""
Program for storing to do lists by JSON
"""
import os
import display
from run import run
from models import Task


def main():
    """get_tasks returns Task object containing:
    - date of task (only when creating)
    - name of target
    - priority: bool
    - completed: bool
    - command: exit/new/delete/modify/complete
    with separate functions for each command
    note that all other branches return None if exit"""

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        task = display.get_tasks()
        if task == Task(command="exit"):
            break
        run(task)


if __name__ == "__main__":
    main()
