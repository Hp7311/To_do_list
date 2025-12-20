"""core of app. Process specific to command"""

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
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(name)s | %(message)s")
logger = logging.getLogger(__name__)

if os.getcwd().endswith("To_do_list/src"):
    JSON_PATH = "data.json"
elif os.getcwd().endswith("To_do_list"):
    JSON_PATH = "src/data.json"
else:
    raise FileNotFoundError("Not in correct directory")

MAX_NAME = os.get_terminal_size().columns - 53

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
    if len(name) > MAX_NAME:
        print("Name too long")
        return new
    if name in names:
        print("Already a task with same name.")
        return new # SOLVED: new() doesnt restart, it runs new() inside if name in names
    task.name = name
    logger.info("Task: %s", task)

    print("Assign a unique ID to it")
    new_num = input("> ").strip()
    try:
        null = int(new_num)
        del null
    except ValueError:
        print("Enter a number")
        return new
    if new_num in numbers:
        print("ID already assigned")
        return new
    if int(new_num) > 100:
    	print("ID too big.")
    	return new
    task.number = new_num
    logger.info("Task: %s", task)

    print("When is it due? yyyy-mm-dd")
    date = input("> ").strip()
    if not date_valid(date):
        print("Not a date")
        return new
    task.date = date
    logger.info("Task: %s", task)

    print("Should it be marked as important? y")
    important = input("> ").strip().lower()
    if important == "y":
        task.priority = True
    else:
        task.priority = False

    task.completed = False
    logger.info("Task: %s", task)

    # writes to file
    task.save()


def modify():
    existing_tasks: dict = task_class.get_contents()
    task = task_class.Task()
    logger.info("Initial task: %s", task)

    # ask which one to modify
    print("Enter the ID of the task you want to modify.")
    number = input("> ").strip()
    if number not in existing_tasks:
        print(f"No task found for {number}")
        return modify

    # Get other info of the task
    task.number = number
    task.name, task.date, task.priority, task.completed = existing_tasks[task.number]
    logger.info("task after selecting: %s", task)

    # modify the dict
    print("Enter new name, Enter if remain unchanged.")
    new_name = input("> ").strip()
    if len(new_name) > MAX_NAME:
    	print("Name too long")
    	return modify
    if new_name != "":
        task.name = new_name
    logger.info("task after mod. name: %s", task)

    print("Change priority? y if change.")
    change_priority = input("> ").strip().lower()
    if change_priority == "y":
        if task.priority:
            task.priority = False
        else:
            task.priority = True
    logger.info("task after mod. priority: %s", task)

    print("Enter new ID, Enter if remain unchanged")
    new_number = input("> ").strip()
    try:
        null = int(new_number)
        del null
    except ValueError:
        if new_number != "":
            print("Enter a number")
            return modify()
    if int(new_number) > 100:
    	print("ID too big.")
    	return new
    if new_number in existing_tasks:
        print("Number already assigned.")
        return modify()
    if new_number != "":
        task.number = new_number
        delete_original_task_for_key(
            number
        )  # deletes dict key-value with chosen number from JSON
    logger.info("task after mod. priority: %s", task)

    # write back
    task.save()


def delete():
    existing_tasks: dict = task_class.get_contents()

    print("Enter ID of the task that you want to delete.")
    delete_num = input("> ").strip()

    try:
        null = int(delete_num)
    except ValueError:
        print("Enter a number")
        return delete
    if delete_num not in existing_tasks:
        print(f"Task with ID: {delete_num} does not exist.")
        return delete

    existing_tasks.pop(delete_num)  # delete

    logger.info("task about to be saved after deleted: %s", existing_tasks)
    with open(JSON_PATH, "w") as file:
        json.dump(existing_tasks, file)  # save changes


def complete():
    existing_tasks = task_class.get_contents()
    task = task_class.Task()

    print("Enter ID of the task to complete.")
    complete_num = input("> ").strip()

    try:
        null = int(complete_num)
        del null
    except ValueError:
        print("Enter a number")
    if complete_num not in existing_tasks:
        print(f"task with ID {complete_num} does not exist")
        return delete

    name, date, priority, completed = existing_tasks[complete_num]
    delete_original_task_for_key(complete_num)
    if completed:
        print("Already completed.")
        return delete
    task.number = complete_num
    task.name = name
    task.date = date
    task.priority = priority
    task.completed = True
    logger.info("task after completing %s", task)

    task.save()


def exit():
    """remember to handle"""
    return


def date_valid(s) -> bool:
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def delete_original_task_for_key(key):
    """deletes given key-value in JSON_PATH"""
    with open(JSON_PATH) as file:
        tasks = json.load(file)
    tasks.pop(key)
    with open(JSON_PATH, "w") as write_file:
        json.dump(tasks, write_file, indent=4)
