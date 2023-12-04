#!/bin/bash

# Script Name:                  compress-o-matic
# Author:                       Zachariah Woodbridge
# Date of latest revision:      03 Dec 2023
# Purpose:                      bash script that clears-out log files.
# ChatGPT helped my code by showing me how to add for loops as opposed to doing the compression/checking manually, otherwise its me.

# Declaration of variables
 
# backup directory location
backup_dir="$HOME/backups-syslogs"

# create timestamptimestamp
timestamp=$(date +"-%Y%m%d%H%M%S")

# Declaration of functions

# Function to check and create backup directory
CheckDir() {
  [ -d "$backup_dir" ] || mkdir -p "$backup_dir"
  echo "Backup directory exists: $backup_dir"
}

# Main

CheckDir

# Print to the screen the file size of the log files before compression
for file in /var/log/syslog /var/log/wtmp; do
  original_size=$(du -h "$file" | awk '{print $1}')
  echo "Size of $file before compression: $original_size"
done

# Compress the contents of the log files to the backup directory
zip_filename="syslogs${timestamp}.zip"
zip -r "$backup_dir/$zip_filename" /var/log/syslog /var/log/wtmp

# Clear the contents of the log file
for file in /var/log/syslog /var/log/wtmp; do
  sudo truncate -s 0 "$file"
done

# Print to screen the file size of the compressed file
for file in /var/log/syslog /var/log/wtmp; do
  compressed_size=$(du -h "$file" | awk '{print $1}')
  echo "Size of $file after compression: $compressed_size"
done

# Compare the size of the compressed files to the size of the original log files
echo "Comparison:"
echo "  Before compression: $original_size"
echo "  After compression:  $compressed_size"
