# Script Name:                  Challenge 06
# Author:                       Zachariah Woodbridge
# Date of latest revision:      05 Dec 2023
# Purpose:                      More practice using python, in this case printing a huge list of directories and files.

# Declaration of imports
import os

# Declaration of variables
path = input("Please provide a file path: ")
# Declaration of functions

# Function that prints the directory path, directory name(s), and file name(s) as per the Main command
def generate_directory(path):
    for dirpath, dirname, filename in os.walk(path):
        print(f'Directory: {dirpath}')
        for dirname in dirname:
            print(f'Sub-Directory: {dirname}')
        for filename in filename:
            print(f'File: {filename}')

# Main
if __name__ == "__main__":
    generate_directory(path)
# End
