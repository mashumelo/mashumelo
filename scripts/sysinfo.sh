#!/bin/bash

clear
echo “This information is brought to you by $0.”
echo
#Welcome the user
echo “Welcome, $USER”
echo
echo “Today is `date`.”
echo
#operating system info is obtained from uname command
echo “Operating System:”
uname -o
echo
#System information obtained from uname command
echo “This is `uname -s` running on a `uname -m` processor.”
echo
#cpu info is obtained from lscpu command
echo “CPU Info:”
lscpu
echo
#kernel version
echo “Kernel Version:”
echo “The kernel version is: `uname -r` ”
echo
#Information of uptime
echo “Now showing uptime information:”
uptime
echo
#Showing free memory
echo “Memory Details:”
free
echo
#Disk space usage obtained from df command
echo “Disk Space Usage:”
df -mh
echo 
$SHELL