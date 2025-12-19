"""core of app. Process according to command """
"""JSON style:
	{
		<number>:
		[
		    <name>,
		    <date>,
		    <priority>,
		    <completed>,
		]
	}"""
import json
import models as task_class
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(name)s | %(message)s")
logger = logging.getLogger(__name__)

JSON_PATH = "data.json"


def new():
    """adds another task"""

    existing_tasks = task_class.get_contents()

    numbers = list()
    names = list()
    for num, k in existing_tasks.items():
        numbers.append(num)
        names.append(k[0])

    logger.info("exist numbers: %s", numbers)
    logger.info("exist names: %s", names)

    task = task_class.Task()

    # gets task info and validate
    print("What is the name of the task?")
    name = input("> ").strip()
    if len(name) > 100:
        print("Name too long")
        new()
    if name in names:
        print("Already a task with same name.")
        new()
    task.name = name

    print("Assign a unique number to it")
    new_num = input("> ").strip()
    try:
        null = int(new_num)
        del null
    except ValueError:
        print("Enter a number")
        new()
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

    # ask which one to modify


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
