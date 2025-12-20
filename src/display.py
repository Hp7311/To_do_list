"""get_tasks() returns Task to be parsed and called -> run"""

import json
import os
import models

COMMAND_DICT = {
        "a": "new",
        "b": "modify",
        "c": "delete",
        "d": "complete",
        "e": "exit",
    }
    
if os.getcwd().endswith("To_do_list/src"):
	JSON_PATH = "data.json"
elif os.getcwd().endswith("To_do_list"):
	JSON_PATH = "src/data.json"
else:
	raise FileNotFoundError("Not in correct directory")

def get_tasks() -> models.Task:
    """displays UI and asks for action"""

    display()

    # asks for action
    print()
    print("Do you want to:")
    print("\ta) Create a new task")
    print("\tb) Modify a task")
    print("\tc) Delete a task")
    print("\td) Complete a task")
    print("\te) Exit")
    command = input("> ").strip().lower()
	
    try:
    	return models.Task(command=COMMAND_DICT[command])
    except KeyError:
    	print("Invalid command")
    	return


def display(file_path=JSON_PATH):
    # print current to-do list content

    tasks: dict = models.sort()

    largest_name = 0
    for k, v in tasks.items():
        name = v[0]
        if len(name) > largest_name:
            largest_name = len(name)
    LENGTH = largest_name + 4 + 1 + 13 + 1 + 10 + 1 + 11 + 1 + 10 + 1

    print("Welcome to the To-Do List utility")
    print("-" * LENGTH)
    print()
    print(
        "ID".center(10),
        "|",
        "Name".center(largest_name + 4),
        "|",
        "Date".center(13),
        "|",
        "Priority".center(10),
        "|",
        "Completed".center(11),
        "|",
        sep="",
    )
    print("-" * LENGTH)

    for k, v in tasks.items():
        num = k
        name, date, priority, completed = v

        print(str(num).center(10), end="|")
        print(name.center(largest_name + 4), end="|")
        print(date.center(13), end="|")
        if priority:
            print("⚠️".center(10), end="|")
        else:
            print(" ".center(10), end="|")

        if completed:
            print("✅".center(11), end="|\n")
        else:
            print("✖️".center(11), end="|\n")
    print("-" * LENGTH)

