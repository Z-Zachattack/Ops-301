# Script Name:                  Ops-301d10: Challenge 07
# Author:                       Zachariah Woodbridge
# Date of latest revision:      12/06/2023
# Purpose:                      Python: Lists and Slices

# Declaration of variables

# Declaration of functions

# Declaration of lists

# Creates a list of fruits 
veggies = ["Beets", "Beans", "Broccoli", "Brussels Sprouts", "Bell Peppers", "Bok Choy", "Black Eyed Peas", "Boniato", "Brooklime", "Butternut Squash"]

# Main

# Prints the first element
print("Fourth Veggie:", veggies[3])

# Prints the sixth through tenth
print("Sixth Through Tenth Fruits:")
for veggie in veggies[5:10]:
    # Prints each fruit
    print(veggie)

# Adds an element to the list
veggies[6] = "onion"
# Prints the updated value
print("Updated Seventh Element:", veggies[6])

# Prints the entire list
print ("New List:", veggies)

# End
