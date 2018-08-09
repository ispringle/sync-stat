# sync-stat
Sync Statuses across Slack Workspaces

## Usage
`python sync-status.py`
 - This will walk you through the process of updating a status, emoji selection, and syncing status to 
workspaces on file

`python sync-staus.py add`
 - This will ask you for a nickname for a workspace and either the [Legacy Token](https://api.slack.com/custom-integrations/legacy-tokens) or the sync-stat app API token. 
 It will then ask to set a status.

## Dependencies
 - Python 3.x
 - pickle
 - slackclient

