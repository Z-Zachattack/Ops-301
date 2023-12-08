# Script Name:                  Ops-301d10: Challenge 08
# Author:                       Zachariah Woodbridge
# Date of latest revision:      07 Dec 2023
# Purpose:                      Python: Conditional Statements

import random
# Declaration of variables

a = random.randrange(1, 4)
b = 2*a
c = 2+a
d = 4
# Declaration of functions

# Main
if d >= a:
    print("ready")
if d > a:
    print("set")   
if a!= d:
    print("go")
if b == c:
    print("a equals 2")
elif b > c:
    print("a equals 3")
elif b < c:
    print("a equals 1")
else:
    print("a equals 0")
# End
