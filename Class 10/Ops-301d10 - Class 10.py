# Script Name:                  Ops-301d10 - Class 10
# Author:                       Zachariah Woodbridge
# Date of latest revision:      10 Dec 2023
# Purpose:                      Ops Challenge: Python File Handling

# I used chatGPT to clean up my code, it also found one mistake (mispelling). Otherwise, all me.
import os

# Declaration of variables
file_name = "new.txt"
writefile = open(file_name, "w")
readfile = open(file_name, "r")

# Declaration of functions
lines = ["Line 1", "Line 2", "Line 3"]

# Main 
# Appends three lines to the file
for line in lines:
    writefile.write(line + "\n")

# Closes the file after writing
writefile.close()

# Opens the file again in read mode to read the first line
readfile = open(file_name, "r")
first_line = readfile.readline()

# Prints the first line
print("First line:", first_line)

# Closes the file after reading
readfile.close()

# Delete the file
os.remove(file_name)

print(file_name, "has been deleted")
# End
