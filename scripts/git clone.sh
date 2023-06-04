#!/bin/bash

#changes directory to your home directory
cd ~/
#prompts for the repository link
echo "What is the link to the repository you'd like to clone? "
#take user input
read REPO
#prompts for repository name
echo "What is the name of your repository? "
read REPO_NAME
#clones your github repo
echo "Cloning git repo!"
git clone ${REPO}
echo "Repo successfully cloned!"
#adds your official repo to be committed
git add ~/${REPO_NAME}
#changes to folder directory
cd ~/${REPO_NAME}
#commits all changes and prompts with a message
git commit -m 'git repo cloned to new pc using clone script'
#pushes your clone changes to github
git push origin main
#confirms you have cloned your github repo
echo "You have successfully cloned your github repo!"