#!/bin/bash

# Make executable with chmod +x <<filename.sh>>
CURRENTDIR=${pwd}
#name of the remote repo. Enter a single word or separate with hyphens
echo "What name do you want to give your remote repo?"
#take user input
read REPO_NAME
#repo description
echo "Enter a repo description: "
read DESCRIPTION
#the project folder path
echo "what is the path to your local project directory?"
read PROJECT_PATH
#github username
echo "What is your github username?"
read USERNAME
#go to the path 
cd "$PROJECT_PATH"
#initialise the repo locally, create blank README, add and commit the repo
git init
touch README.md
git add README.md
#commit the git with a message of choice
git commit -m 'git initialized with init script'
#github API to log the user in
curl -u ${USERNAME} https://api.github.com/user/repos -d "{\"name\": \"${REPO_NAME}\", \"description\": \"${DESCRIPTION}\"}"
#add the remote github repo to local repo and push
git remote add origin https://github.com/${USERNAME}/${REPO_NAME}.git
git push --set-upstream origin main
#change to your project's root directory.
cd "$PROJECT_PATH"
echo "Done. Go to https://github.com/$USERNAME/$REPO_NAME to see."
echo "You're now in your project root."
$SHELL