vcs
===

VCS saves and restores snapshots of the directory from which it's called.  It's a toy system; don't use it for data you care about!  

The examples below assume you've made the vcs file executable and put it somewhere in your path.  If you don't want to do that, you'll have to feed it to python directly, for example using `../python vcs foo` instead of `vcs foo` in the provided test directory.

`vcs help` will list the currently available commands.  It's pretty self-explanatory if you've used git before.

To try it out, clone this (git) repo, and initialize a (vcs) repo in the test directory with `vcs init`.  This will create an empty `.vcs` directory, which you can look around in if you like.  It's a (much) simplified version of the kind of thing git stores in `.git`.

Create a backup with `vcs backup [message]`.  The backup message is optional.  Now change one of the files and make another backup.  `vcs log` will print out the date, time, and message of both backups, along with their message if you entered any.

You can revert to the first snapshot with `vcs checkout 1`.  Now make another backup and run `vcs log`.  It will not show any information about backup number 2, because 2 is on a different branch of the revision history.  At the moment branches are not named, so you have to know the id of the head of the branch you want to switch to (in this case 2).




