"""
Program for storing to do lists by JSON
"""
import os
import display
from run import run
from models import Task


def main():
    """
    clear screen
    get a Task class containing command
    run module calls the corresponding function in operations
    """

    while True:
        #os.system("cls" if os.name == "nt" else "clear")
        task = display.get_tasks()
        if task.command == "exit":
            break
        run(task)


if __name__ == "__main__":
    main()
