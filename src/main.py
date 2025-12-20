"""
Program for storing to do lists by JSON
"""

import os
import logging
import display
from run import run

DISABLE_LOGGING =True
CLEAR = True

if DISABLE_LOGGING:
	logging.disable(logging.CRITICAL)

def main():
    """
    clear screen
    get a Task class containing command
    run module calls the corresponding function in operations
    """

    while True:
        try:
            if CLEAR:
        	     os.system("cls" if os.name == "nt" else "clear")
            task = display.get_tasks()  # calls display returns Task
            if task.command == "exit":
     	       break
            if task.command == "restart":
       	     continue
            
            func = run(task)  # calls operation returns None or operation._
            while func:
                print()
                func = run(task)  # repeats
        	    
        	    
        except EOFError:
            break


if __name__ == "__main__":
    main()
