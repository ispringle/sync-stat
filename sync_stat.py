#!/usr/bin/env python
'''
sync-stat - Sync a status to multiple workspaces from the command line
Version: 0.1.1
'''

import pickle
from slackclient import SlackClient
import sys
import argparse

class Post(object):
	
	def __init__(self, status, workspaces):
		self.update_status(status, workspaces)
	
	def update_status(self, status, workspaces):
		for space in workspaces:
			sc = SlackClient(space['auth'])
			sc.api_call(
				"users.profile.set",
				profile = status
				)

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
				self.spaces = pickle.load(open('spaces.p', 'rb'))
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
	
	def select_workspaces(self):
		syncTo = []
		for workspace in self.spaces:
			selection = input("Sync status to %s? [y/n]" % workspace)
			if selection == "y" or selection == "Y" or selection == "yes":
				syncTo.append(self.spaces[workspace])
		return syncTo
	
	def select_all(self):
		syncTo = []
		for workspace in self.spaces:
			syncTo.append(self.spaces[workspace])
		return syncTo

def parse():
	parser = argparse.ArgumentParser(description="Post status to multiple workspaces at once")
	parser.add_argument('-a', '--add', help="Add a new workspace", dest='add', action='store_true')
	parser.add_argument('-s', '--status', help="Status to sync", dest='status')
	parser.add_argument('-w', '--workspaces', help="Workspaces to sync to, by nickname or 'all' for all spaces",
						dest='workspaces')
	parser.add_argument('-e', '--emoji', help="Emoji to sync", dest='emoji')
	
	return vars(parser.parse_args())

def main(argv):
	#Load workspaces if they exist, query to add workspaces if they do not
	work = Spaces()
	
	args = parse()
	if args['add'] == True:
		Spaces.add_workspace()

	if args['status'] != None:
		if args['emoji'] != None:
			status = { "status_text" : args['status'], "status_emoji" : args['emoji'] }
		else:
			status = { "status_text" : args['status'], "status_emoji" : "" }
	else:
		status = Status.set()
	
	if args['workspaces'] != None:
		if args['workspaces'] == "all":
			toSync = work.select_all()
	else:
		toSync = work.select_workspaces()
	
	#Get status, select workspaces to sync to, and post to selected workspaces
	Post(status, toSync)

if __name__ == "__main__":
	main(sys.argv)

