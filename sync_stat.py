#!/usr/bin/env python

import pickle
from slackclient import SlackClient
inport sys

if __name__ == "__main__":
	main(sys.argv)


def update_status(status, workspaces):
	for space in workspaces:
		sc = SlackClient(space['auth'])
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
	for workspace in Spaces.spaces:
		selection = input("Sync status to %s? [y/n]" % workspace)
		if selection == "y" or selection == "Y" or selection == "yes":
			syncTo.append(Spaces.spaces[workspace])
	return syncTo

class Spaces(self):
	
	def __init__(self):
		try:
			self.spaces = pickle.load( open('spaces.p', 'rb'))
		except:
			add_workspace()
			self.spaces = pickle.load( open('spaces.p', 'rb'))
	
def add_workspace():
	spaces = {}
	add = True
	while add:
		workspace = input("Workspace nickname: ")
		client = input("What chat client is this for? [Slack/Discord]: ")
		token = input("Workspace legacy token or App token: ")
		spaces[workspace] = { "auth" : token, "client" : client }
		next = input("Add another workspace?: [y/n]")
		if next == 'y' or next == "Y" or next == "yes":
			pass
		else:
			add = False
	pickle.dump(spaces, open("spaces.p", "wb"))

status = set_status()
syncTo = select_workspaces()
print("Posting status")
update_status(status, syncTo)

def main():
	try:
		pickle.load( open('spaces.p', 'rb'))
		spaces = Spaces():
	except:
		makeNew = input("No workspaces found. Would you like to setup a workspace?[y/n]: ")
		if makeNew = 'y' or makeNew = 'Y' or makeNew = 'yes' or makeNew = 'Yes' or makeNew = 'YES':
			spaces = Spaces()
		else:
			quit()
#try:
#	script, option = argv
#	if option == "add":
#		add_workspace()
#except:
#	pass

