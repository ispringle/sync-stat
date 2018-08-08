import pickle
from slackclient import SlackClient
from sys import argv

def update_status(status, workspaces):
	for token in workspaces:
		sc = SlackClient(token)
		sc.api_call(
			"users.profile.set",
			profile = status
			)

def set_status():
	status = input("Status: ")
	emoji  = input("Emoji: ")
	return { "status_text" : status, "status_emoji" : emoji }

def select_workspaces():
	syncTo = []
	for workspace in spaces.Spaces:
		selection = input("Sync status to %s? [y/n]" % workspace)
		if selection == "y" or selection == "Y" or selection == "yes":
			syncTo.append(spaces.Spaces[workspace])
	return syncTo

def add_space():
	Spaces = {}
	add = True
	while add:
		workspace = input("Workspace nickname: ")
		token = input("Workspace legacy token or App token: ")
		Spaces[workspace] = token
		next = input("Add another workspace?: [y/n]")
		if next == 'y' or next == "Y" or next == "yes":
			pass
		else:
			add = False
	pickle.dump(Spaces, open("Spaces.p", "wb"))
try:
	script, option = argv
	if option == "add":
		add_space()
except:
	pass

class spaces:
	Spaces = pickle.load( open("Spaces.p", "rb"))

status = set_status()
syncTo = select_workspaces()
print("Posting status")
update_status(status, syncTo)
