"""
Program for storing to do lists by JSON
"""

import sys
from display import get_tasks
import operations


def main():
	"""get_tasks returns Task object containing:
	- date of task (only when creating)
	- name of target
	- priority: bool
	- completed: bool
	- command: exit/new/delete/modify/complete
	with seperate functions for each command
	note that all other branches return None if exit"""
	
	task = get_tasks()
	
	if task.get_command == operations.exit:
		sys.exit()
		
	operation = task.get_command()
	print("got operation command of", operation)
	operation()
	print("reached end")
	
if __name__ == "__main__":
	main()
