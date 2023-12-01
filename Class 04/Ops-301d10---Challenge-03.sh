#!/bin/bash

# Script Name:                  Change file permissions
# Author:                       Zachariah Woodbridge
# Date of latest revision:      30-Nov-2023
# Purpose:                      Boolean Conditionals

# Declaration of variables
hello="1. Hello world!"
ping="2. Ping yo'self"
ipinfo="3. IP Info"
exit="4. Exit"
# Declaration of functions

# Main
while true; do
    clear
    read -p "What can I do for you? Please choose a number" choice
    echo "$hello"
    echo "$ping"
    echo "$ipinfo"
    echo "$exit"
    read choice

    if [[ $choice == 1 ]]; then
        echo "Hello World"
        # The -p option is used with the read command to display a prompt to the user and wait for them to enter input.
        read -p "Press Enter to continue"
    elif [[ $choice == 2 ]]; then
        ping -c 4 127.0.0.1
        read -p "Press Enter to continue"
    elif [[ $choice == 3 ]]; then
        ip a
        read -p "Press Enter to continue"
    elif [[ $choice == 4 ]]; then
        echo "Exiting"
        exit 0
    else
        echo "Invalid choice"
        read -p "Press Enter to continue"
    fi
done
