"""actually processes whatever is required"""
import json
import task as task_module

JSON_PATH = "../data/data.json"

def new():
    """adds another task"""
    try:
	    with open(JSON_PATH) as f:
	        tasks: dict = json.load(f)
	    	
    except FileNotFoundError:
        with open("data/data.json") as f:
            tasks: dict = json.load(f)
    numbers = list()
	for k,v in existing_tasks.items():
		numbers.append(v[3])
	
	task = task_module.Task()
	
	# gets task info and validate
	print("What is the name of the task?")
	name = input("> ").strip()
	if len(name) > 100:
		print("Name too long")
		new()
	if name in existing_tasks:
		print("Already a task with same name.")
		new()
	print("Assign a unique number to it")
	new_num = int(input("> ").strip())
	if new_num in numbers:
		print("Number already assigned")
		new()
	task.number = new_num
	task.name = name
		
	print("When is it due? dd/mm/yyyy")
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
	with open(JSON_PATH) as file:
		tasks: dict = json.load(file)
		
	# debugging
	print(tasks)
	
	tasks[task.name] = [task.date, task.priority, task.completed, task.number]
	
	with open(JSON_PATH, "w") as file:
		json.dump(tasks, file, indent=4)
		
	
def modify():
	...
	
def delete():
	...
	
def complete():
	...

def exit():
	"""remember to handle"""
	pass
	
from datetime import datetime

def date_valid(s) -> bool:
    try:
        datetime.strptime(s, "%d/%m/%Y")
        return True
    except ValueError:
        return False
