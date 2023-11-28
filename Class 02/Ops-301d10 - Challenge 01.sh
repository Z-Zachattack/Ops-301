#!/bin/bash

# Script Name:                  Syslog+Append
# Author:                       Zachariah Woodbridge
# Date of latest revision:      28-Nov-2023
# Purpose:                      Copy and Append

# Declaration of variables
# Define the source file path
source="/var/log/syslog"

# Generate the date and time suffix using the format %m-%d-%Y
date=$(date +"%m-%d-%Y")

# Defines destination file (the syslog file with the date suffix)
destination="syslog_${date}.log"

# Declaration of functions
# Main

# Copy the source file to the destination file
cp "$source" "$destination"
# End
