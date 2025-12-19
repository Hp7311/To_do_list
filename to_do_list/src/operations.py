"""core of app. Process according to command """
"""JSON style:
	{
		<name>:
		[<date>,
		<priority>,
		<completed>
		<number>],
	}"""
import json
import models as task_class


JSON_PATH = "data.json"


def new():
    """adds another task"""

    existing_tasks = task_class.get_contents()
    numbers = list()
    for k, v in existing_tasks.items():
        numbers.append(v[3])

    task = task_class.Task()

    # gets task info and validate
    print("What is the name of the task?")
    name = input("> ").strip()
    if len(name) > 100:
        print("Name too long")
        new()
    if name in existing_tasks:
        print("Already a task with same name.")
        new()
    task.name = name

    print("Assign a unique number to it")
    new_num = int(input("> ").strip())
    if new_num in numbers:
        print("Number already assigned")
        new()
    task.number = new_num

    print("When is it due? yyyy-mm-dd")
    date = input("> ").strip()
    if not date_valid(date):
        print("Not a date")
        new()
    task.date = date

    print("Should it be marked as important? y/n")
    important = input("> ").strip().lower()
    if important == "y":
        task.priority = True
    elif important == "n":
        task.priority = False

    # writes to file
    task.save()


def modify():
    existing_tasks = task_class.get_contents()


def delete(): ...


def complete(): ...


def exit():
    """remember to handle"""
    pass


from datetime import datetime


def date_valid(s) -> bool:
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False
