#!/bin/bash
cd ~/ || exit
LIST_OF_APPS=""
echo "Which distro are you running? Fedora, Ubuntu (Choose for Linux Mint, Pop!_OS, or other Ubuntu derivatives.) or Arch? "
read DISTRO
echo "Would you like to update the system? "
read UPDATE
#if {UPDATE} is yes

if [ "${DISTRO}" == Arch ]
then
    if [ "${UPDATE}" == yes ]
    then
        echo "The system will be upgraded."
        #updates the repositories and whole system
        sudo pacman -Syu
        echo "The system will now install the listed apps."
        sudo pacman -S "${LIST_OF_APPS}" -y
    #if {UPDATE} is no
    elif [ "${UPDATE}" == no ]
    then
        echo "The system will not be upgraded."
        #updates the repositories
        sudo pacman -Sy
        echo "The system will now install the listed apps."
        sudo pacman -S "${LIST_OF_APPS}" -y
    #otherwise print "Invalid Choice!"
    else ${UPDATE}
    echo "Invalid Choice!"

fi
elif [ "${DISTRO}" == Fedora ]
then
    if [ "${UPDATE}" == yes ]
    then
        echo "The system will be upgraded."
        #updates the repositories and whole system
        sudo dnf update
        echo "The system will now install the listed apps."
        sudo dnf install "${LIST_OF_APPS}" -y
    #if {UPDATE} is no
    elif [ "${UPDATE}" == no ]
    then
        echo "The system will not be upgraded."
        #updates the repositories
        sudo dnf check-update
        echo "The system will now install the listed apps."
        sudo dnf install "${LIST_OF_APPS}" -y
    #otherwise print "Invalid Choice!"
    else ${UPDATE}
    echo "Invalid Choice!"
fi
if [ "${DISTRO}" == Ubuntu ]
then
    if [ "${UPDATE}" == yes ]
    then
        echo "The system will be upgraded."
        #updates the repositories and whole system
        sudo apt full-upgrade
        echo "The system will now install the listed apps."
        sudo apt install "${LIST_OF_APPS}" -y
    #if {UPDATE} is no
    elif [ "${UPDATE}" == no ]
    then
        echo "The system will not be upgraded."
        #updates the repositories
        sudo apt update
        echo "The system will now install the listed apps."
        sudo apt install "${LIST_OF_APPS}" -y
    #otherwise print "Invalid Choice!"
    else ${UPDATE}
    echo "Invalid Choice!"

fi
else
echo "Please choose Fedora, Ubuntu or Arch."
fi
$SHELL