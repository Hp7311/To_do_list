"""One public API: get_tasks() returns Task to be called methods"""
import json

def get_tasks():
	"""displays UI and asks for action"""
	"""JSON style:
	{
		<name>:
		[<date>,
		<priority>,
		<completed>
		<number>],
	}"""
	
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
	COMMAND_DICT = {
		"a": "new",
		"b": "modify",
		"c": "delete",
		"d": "complete",
		"e": "exit"
	}
	
	return Task(command = COMMAND_DICT[command])
	

	
def display(file_path = "../data/data.json"):
	# print current to-do list content

	try:
	    with open(file_path) as f:
	    	tasks: dict = json.load(f)
	except FileNotFoundError:
	     with open("data/data.json") as f:
	        tasks: dict = json.load(f)
    
	
	largest_name = 0
	for name in tasks:
		if len(name) > largest_name:
			largest_name = len(name)
	LENGTH = largest_name + 4 + 1 + 13 + 1 + 10 + 1 + 11 + 1 + 10 + 1
			
	print("Welcome to the To-Do List utility")
	print("-" * LENGTH)
	print()
	print("ID".center(10), "|",
			  "Name".center(largest_name + 4), "|",
		 	 "Date".center(13), "|",
			  "Priority".center(10), "|",
			  "Completed".center(11), "|", sep="")
	print("-" * LENGTH)
	for k,v in tasks.items():
		date, priority, completed, num = v
		
		print(str(num).center(10), end="|")
		print(str(k).center(largest_name + 4), end="|")
		print(str(date).center(13), end="|")
		if priority:
			print("⚠️".center(10), end="|")
		else:
			print(" ".center(10), end="|")
		
			
		if completed:
			print("✅".center(11), end="|\n")
		else:
			print("✖️".center(11), end="|\n")
	print("-" * LENGTH)
	

#get_tasks()
