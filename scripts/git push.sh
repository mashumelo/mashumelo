#!/bin/bash

#changes to home directory
echo "Changing to home directory!"
cd ~/
#prompts for which directory you'd like to move to
echo "Which directory would you like to move to? "
#take user input
read REPO
#change to that directory
echo "Changing to repo directory."
cd ~/${REPO}
#prompts for folders and files you'd like to add before committing
echo "What folders or files would you like to add for changes?"
read FOLDERS_AND_FILES
#adds any folders with changes required
git add ${FOLDERS_AND_FILES}
#commits all changes with a personal message
echo "Committing all changes, please enter commit message. "
git commit -a
#pushes the repository
echo "Pushing the repository to github"
git push
#echoes an output message that it was successful.
echo "git repo successfully pushed to the server!"
$SHELL