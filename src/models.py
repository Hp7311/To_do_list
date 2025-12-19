"""class Task with functions to load and save JSON"""
import json
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(name)s | %(message)s")
logger = logging.getLogger(__name__)
#logging.disable(logging.CRITICAL)


def get_contents(file_path="data.json") -> dict:
    with open(file_path) as file:
        og: dict = json.load(file)
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


    def save(self, file_path="data.json"):
        # Read json
        with open(file_path) as file:
            og = json.load(file)
        # Edit/create json
        og[self.number: str] = [self.name, self.date, self.priority, self.completed]

        logger.info("Dict about to be saved: %s", og)
        # Save json
        with open(file_path, "w") as file:
            json.dump(og, file, indent=2)
