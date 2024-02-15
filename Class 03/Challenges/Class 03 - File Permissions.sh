#!/bin/bash

# Script Name:                  Permission-changer
# Author:                       Zachariah Woodbridge
# Date of latest revision:      28-Nov-2023
# Purpose:                      Bashing through permissions
# Everything is mine, but I did use chatGPT to help with the if loop.

# Declaration of variables
# Define the source file path
DirP=()
PerNum=()

# Declaration of functions

# Main

# Prompts user for input directory path.
read -p "What Directory would you like to change the permissions of? " DirP

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
read -p "Input Permissions Number: (e.g. 777 to perform a chmod 777)" PerNum

# Zach's Improvement: I double checked with chatGPT
read -p "Are you sure you want to change permissions in '$DirP' to '$PerNum'? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "Permission change aborted."
    exit 0
fi

# Navigates to the directory input by the user and changes all files inside it to the input setting.
cd "$DirP"
chmod -R "$PerNum" "./"

# Prints to the screen the directory contents and the new permissions settings of everything in the directory.
sleep 1
echo "Changing permissions in '$DirP' to '$PerNum'..."
ls -al "$DirP"

# End