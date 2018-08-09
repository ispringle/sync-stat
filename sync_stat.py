#! /usr/bin/env python

import pickle
from slackclient import SlackClient
from sys import argv

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

try:
	script, option = argv
	if option == "add":
		add_workspace()
except:
	pass

class Spaces:
	spaces = pickle.load( open("spaces.p", "rb"))

status = set_status()
syncTo = select_workspaces()
print("Posting status")
update_status(status, syncTo)
