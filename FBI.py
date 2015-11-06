"""
FBI.py

Eric Sund
November 4, 2015

This program figures out where Sherlock Holmes could bury 8 bones for his dog
in a 15x12 grid of length 6.
"""

#import modules
import re, random

orientations = ['up', 'down', 'left', 'right']
bones = [] #locations to store for the buried bones

#create the 15x12 matrix for the yard with all the bones to display
yard = [["." for x in range(15)] for x in range(12)]

#define the functions

def getOrientation():
    return orientations[random.randint(0,3)]

def placeBone():
    if getOrientation() == 'right':
        y = random.randint(0,11)
        x = random.randint(0,8) #bones of length 6 overflow if placed greater than 8
        yard[y][x] = "B"
        for i in range(6):
            yard[y][x + i] = "B"
        return [y, x, 'right']
    elif getOrientation() == 'left':
        y = random.randint(0,11)
        x = random.randint(5,14) #bones of length 6 overflow if placed less than 5
        yard[y][x] = "B"
        for i in range(5, 0, -1):
            yard[y][x - i] = "B"
        return [y, x, 'left']
    elif getOrientation() == 'up':
        y = random.randint(5,11) #bones of length 6 overflow if placed less than 5
        x = random.randint(0,14)
        yard[y][x] = "B"
        for i in range(5, 0, -1):
            yard[y - i][x] = "B"
        return [y, x, 'up']
    elif getOrientation() == 'down':
        y = random.randint(0,6) #bones of length 6 overflow if placed greater than 6
        x = random.randint(0,14)
        yard[y][x] = "B"
        for i in range(6):
            yard[y + i][x] = "B"
        return [y, x, 'down']


def showYard():
    top = ""
    sideNum = 0
    #create the x axis numbers
    for i in range(15):
        if i <= 9:
            top += str(i) + "  " #create one space between double digits
        if i > 9:
            top += str(i) + " "  #create two spaces between single digits
    print(top)

    #create the rows of dots and stick the y axis numbers on the ends of them
    for row in yard:
        print("  ".join(row) + "  " + str(sideNum))
        sideNum += 1

def showBone(boneNumber):
    yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
    if bones[boneNumber-1][2] == 'right':
        for i in range(6):
            #yardToShowBoneIn[index of y][index of x]
            #index of y = bones[boneNumber-1][0]
            #index of x = bones[boneNumber-1][1]
            yardToShowBoneIn[bones[(boneNumber-1)][0]][bones[(boneNumber-1)][1] + i] = "B"

            #display the bone
            for i in range(15):
                if i <= 9:
                    top += str(i) + "  " #create one space between double digits
                if i > 9:
                    top += str(i) + " "  #create two spaces between single digits
            print(top)
            for row in yardToShowBoneIn:
                print("  ".join(row) + "  " + str(sideNum))
                sideNum += 1



#MAIN
print("""Welcome to Sherlock Holmes' and Toby's Fast Bone Investigation (FBI) app.
This app shows possible patterns in which bones can be buried in Mrs. Hudson's backyard!
These "buried bone" patterns can be used to play the Fast Bone Investigation (FBI) game.\n\n
Here is the backyard with 0 bones buried.""")

#show blank yard
showYard()
#bury each bone and remember where it is by appending y and x coordinates and direction in a list
for i in range(8):
    bones.append(placeBone())


#get the valid input with guardian code
running = True
while running:
    choice = input("""\n\nWhere should Sherlock Holmes bury bone x for Toby to find?
Please, enter a bone number from 1 to 8 and this app shall show a location where this bone could be buried.
Enter -1 to quit or 0 to display all bones at once: """)

    if len(choice) == 0:
        print("***You have not entered anything. You need to enter a valid number!")
    elif len(re.findall("[A-Z]", choice)) >= 1 or len(re.findall("[a-z]", choice)) >= 1:
        print("***You have entered " + str(choice) + ".  You need to enter a valid number!")
    elif int(choice) < -1 or int(choice) > 8:
        print("***You have entered " + str(choice) + " which is not in the desired range. You need to enter a valid number!")
    elif int(choice) == -1:
        gettingInput = False
    else:
        choice = int(choice)
        #good to go

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 0:
            showYard()


"""
1.  finish off doing placeBone() for the remaining three directins
2.  Remember the original position of the randomly placed bones at the beginning
    so when it's called again by the user after they display a bone, it's not
    random again like in the beginning.
"""
