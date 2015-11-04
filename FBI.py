"""
FBI.py

Eric Sund
November 4, 2015

This program figures out where Sherlock Holmes could bury 8 bones for his dog
in a 15x12 grid of length 6.
"""

#import modules
import re, sys

print("""Welcome to Sherlock Holmes' and Toby's Fast Bone Investigation (FBI) app.
This app shows possible patterns in which bones can be buried in Mrs. Hudson's backyard!
These "buried bone" patterns can be used to play the Fast Bone Investigation (FBI) game.\n\n
Here is the backyard with 0 bones buried.""")

#display grid
top = ""
sideNum = 0

for i in range(15):
    if i <= 9:
        top += str(i) + "  "
    if i > 9:
        top += str(i) + " "
print(top)

for l in range(12):
    dots = ""
    for w in range(15):
        dots += "." + "  "
        if w == 14:
            dots += str(sideNum)
            sideNum += 1
    print(dots)

#MAIN
#get the valid input

gettingInput = True
while gettingInput:
    choice = input("""\n\nWhere should Sherlock Holmes bury bone x for Toby to find?
Please, enter a bone number from 1 to 8 and this app shall show a location where this bone could be buried.
Enter -1 to quit or 0 to display all bones at once: """)

    #guardian code
    if len(re.findall("[A-Z]", choice)) >= 1 or len(re.findall("[a-z]", choice)) >= 1:
        print("***You have entered " + str(choice) + ".  You need to enter a valid number!")
    elif int(choice) < -1 or int(choice) > 8:
        print("***You have entered " + str(choice) + " which is not in the desired range. You need to enter a valid number!")
    elif int(choice) == -1:
        gettingInput = False
    else:
        gettingInput = False
        choice = int(choice)
