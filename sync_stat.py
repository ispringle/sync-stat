#!/usr/bin/env python

import pickle
from slackclient import SlackClient
import sys

class Post(object):
	
	def __init__(self, status, workspaces):
		syncTo = self.select_workspaces(workspaces)
		self.update_status(status, syncTo)
	
	def update_status(self, status, workspaces):
		for space in workspaces:
			sc = SlackClient(space['auth'])
			sc.api_call(
				"users.profile.set",
				profile = status
				)
	
	def select_workspaces(self, work):
		syncTo = []
		for workspace in work.spaces:
			selection = input("Sync status to %s? [y/n]" % workspace)
			if selection == "y" or selection == "Y" or selection == "yes":
				syncTo.append(work.spaces[workspace])
		return syncTo

class Status(object):
	
	def set():
		status = input("Status: ")
		emoji  = input("Emoji: ")
		return { "status_text" : status, "status_emoji" : emoji }

class Spaces(object):
	
	def __init__(self):
		try:
			self.spaces = pickle.load(open('spaces.p', 'rb'))
		except:
			makeNew = input("No workspaces found. Would you like to setup a workspace?[y/n]: ")
			if makeNew == 'y' or makeNew == 'Y' or makeNew == 'yes' or makeNew == 'Yes' or makeNew == 'YES':
				self.add_workspace()
				spaces = pickle.load(open('spaces.p', 'rb'))
			else:
				quit()
	
	def add_workspace(self):
		spaces = {}
		add = True
		while add:
			workspace = input("Workspace nickname: ")
			#client = input("What chat client is this for? [Slack/Discord]: ")
			client = "Slack"
			token = input("Workspace legacy token or App token: ")
			spaces[workspace] = { "auth" : token, "client" : client }
			next = input("Add another workspace?: [y/n]")
			if next == 'y' or next == "Y" or next == "yes":
				pass
			else:
				add = False
		pickle.dump(spaces, open("spaces.p", "wb"))

def main(argv):
	#Load workspaces if they exist, query to add workspaces if they do not
	work = Spaces()
	
	#Check argv for input
	#Needs to be replaced with an argv parser
	try:
		script, option = argv
		if option == "add":
			Spaces.add_workspace()
	except:
		pass

	#Get status, select workspaces to sync to, and post to selected workspaces
	status = Status.set()
	Post(status, work)

if __name__ == "__main__":
	main(sys.argv)

