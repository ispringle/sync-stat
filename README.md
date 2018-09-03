# sync-stat
Sync Statuses across Slack Workspaces

## Usage
`python sync-status.py`
 - This will walk you through the process of updating a status, emoji selection, and syncing status to 
workspaces on file

`python sync-staus.py -add`
 - This will ask you for a nickname for a workspace and either the [Legacy Token](https://api.slack.com/custom-integrations/legacy-tokens) or ~~the sync-stat app API token~~ (currently only supports Legacy Tokens). 
 It will then ask to set a status.

`python sync-stat.py [-s|--status] "<Status>" [-e|--emoji] :<emoji>: [-w|--workspaces] "<workspaces to sync, or all>"`

If you are using cmus for playing music than you can call the cmus-playing script with `bash cmus-playing`. This
will grab the now playing song using `cmus-remote -Q`, parse this with grep and awk, and then call sync-stat to
sync to all workspaces.

## Dependencies
 - Python 3.x
 - slackclient

## To-Do
 - Current `-w` only accepts "all" need to add ability for `-w` to be used with individual workspace nicknames
