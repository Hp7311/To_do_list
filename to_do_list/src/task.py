"""Task object containing task data. Methods from operations.py"""
import operations

MATCH_FUNCS = {
	"new": operations.new,
	"modify": operations.modify,
	"delete": operations.delete,
	"complete": operations.complete,
	"exit": operations.exit
}

class Task:
	def __init__(self, command=None):
		if command:
			self.command = MATCH_FUNCS[command]
		self.name = None
		self.date = None
		self.priority = None
		self.completed = None
		self.number = None
			
	def get_command(self) -> operations :
		return self.command
