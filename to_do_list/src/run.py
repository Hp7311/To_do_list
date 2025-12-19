"""runs a Task instance, -> operations.py """
import operations
import json

MATCH_FUNCS = {
	"new": operations.new,
	"modify": operations.modify,
	"delete": operations.delete,
	"complete": operations.complete,
	"exit": operations.exit
}

def run(app):
    func = MATCH_FUNCS[app.command]
    func()