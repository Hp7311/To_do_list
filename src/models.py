"""class Task with functions to load and save JSON"""

import json
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(name)s | %(message)s")
logger = logging.getLogger(__name__)

if os.getcwd().endswith("To_do_list/src"):
    JSON_PATH = "data.json"
elif os.getcwd().endswith("To_do_list"):
    JSON_PATH = "src/data.json"
else:
    raise FileNotFoundError("Not in correct directory")


def get_contents(file_path=JSON_PATH) -> dict:
    try:
        with open(file_path) as file:
            og: dict = json.load(file)
        return og
    except FileNotFoundError:
        with open(file_path, "w") as file:
            og = {}
        return og


class Task:
    def __init__(self, command=None):
        self.command = command
        self.name = None
        self.date = None
        self.priority = None
        self.completed = None
        self.number = None

    def get_command(self) -> str:
        return self.command

    def save(self, file_path=JSON_PATH):
        # Read json
        with open(file_path) as file:
            og = json.load(file)
        # Edit/create json
        og[self.number] = [self.name, self.date, self.priority, self.completed]

        logger.info("Dict about to be saved: %s", og)
        # Save json
        with open(file_path, "w") as file:
            json.dump(og, file, indent=4)

    def __repr__(self):
        return f"{self.number}: [{self.name}, {self.date}, {self.priority}, {self.completed}]"


def sort() -> dict:
    """sort JSON"""
    sorted_tasks = dict()
    tasks: dict = get_contents()
    """sorted_index = sorted(tasks.keys())
	for i in sorted_index:
		sorted_tasks[i] = tasks[i]
		
	logger.info("Sorted tasks: %s", sorted_tasks)
	
	with open(JSON_PATH, "w") as file:
		json.dump(sorted_tasks, file, indent=4)
	with open(JSON_PATH) as file:
		cont = json.load(file)
		
	return cont"""
    dates = dict()

    for k, v in tasks.items():
        dates[v[1]] = k  # dict with date: id

    dates_sorted: list = sorted(dates)
    for date in dates_sorted:  # date: "seperate date"
        num = dates[date]
        v = tasks[num]
        sorted_tasks[num] = [v[0], date, v[2], v[3]]  # id: [date ,]

    logger.info("sorted_tasks: %s", sorted_tasks)

    with open(JSON_PATH, "w") as file:
        json.dump(sorted_tasks, file, indent=4)
    with open(JSON_PATH) as file:
        cont = json.load(file)

    return cont
