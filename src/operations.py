"""core of app. Process specific to command """
"""
JSON style:
	{
		<number>:
		[
		    <name>,
		    <date>,
		    <priority>,
		    <completed>,
		]
	}
ALL NUMBERS AND STRINGS ARE APPENDED AS STR
"""
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
    logger.info("Task: %s", task)


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
    logger.info("Task: %s", task)

    print("When is it due? yyyy-mm-dd")
    date = input("> ").strip()
    if not date_valid(date):
        print("Not a date")
        new()
    task.date = date
    logger.info("Task: %s", task)

    print("Should it be marked as important? y/n")
    important = input("> ").strip().lower()
    if important == "y":
        task.priority = True
    elif important == "n":
        task.priority = False
    task.completed = False
    logger.info("Task: %s", task)

    # writes to file
    task.save()


def modify():
    existing_tasks: dict = task_class.get_contents()
    task = task_class.Task()

    # ask which one to modify
    print("Enter the Number of the task you want to modify.")
    number = input("> ").strip()

    # Get other info of the task
    task.number = number
    task.name, task.date, task.priority, task.completed = existing_tasks[task.number]


    # modify the dict
    print("Enter new name, Enter if remain unchanged.")
    new_name = input("> ").strip()
    if new_name != "":
        task.name = new_name

    print("Change priority? y if change.")
    change_priority = input("> ").strip().lower()
    if change_priority == "y":
        if task.priority:
            task.priority = False
        else:
            task.priority = True

    print("Enter new number(id), Enter if remain unchanged")
    new_number = input("> ").strip()
    try:
        null = int(new_number)
    except ValueError:
        if new_number != "":
            print("Enter a number")
            modify()
    if new_number in existing_tasks:
        print("Number already assigned.")
        modify()
    if new_number != "":
        task.name = new_number
        delete_original_task_for_key(number)  # deletes dict key-value with chosen number from JSON


    # write back
    task.save()


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


def delete_original_task_for_key(key):
    with open(JSON_PATH) as file:
        tasks = json.load(file)
    tasks.pop(key)
    with open(JSON_PATH, "w") as write_file:
        json.dump(tasks, write_file)