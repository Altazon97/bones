"""
FBI.py

Eric P. Sund
November 4, 2015

This program figures out where Sherlock Holmes can bury 8 bones of length 6 for
his dog in a 15x12 grid.  Bones can face either vertical or horizontal.  The way
bones are represented on the grid is by changing a "." to a "B" with for loops,
so by sequentially replacing these characters bones can be "drawn" four different
ways.
"""

#import modules
import re, random

#define all the instance variables
orientations = ['up', 'down', 'left', 'right'] #possible directions to "draw" bones
bones = [] #2D list to store locations of the bones
yardWithAllBones = [["." for x in range(15)] for x in range(12)] #create matrix for the yard

#define all the functions
def YardWithOneBoneMsg(howMany):
    """prints message saying this is the yard with one bone
    """
    if howMany == "8":
        print("\nHere is the backyard with " + howMany + " bones buried: ")
    if howMany == "1":
        print("\nHere is the backyard with " + howMany + " bone buried: ")

def getOrientation():
    #Randomly picks and returns a direction for a bone to start being be drawn in
    return orientations[random.randint(0,3)]

def placeBone():
    """
    This function makes use of getOrientation() to decide on a direction for a
    bone to be.  Once known, placeBone() begins sequentially replacing periods
    with Bs to place a bone in the yard for Toby.  x and y coordinate restrictions
    are considered before placing the bone to avoid overflowing out of the yard.
    """
    if getOrientation() == 'right':
        y = random.randint(0,11)
        x = random.randint(0,8) #bones of length 6 overflow if placed greater than 8
        for i in range(6):
            yardWithAllBones[y][x + i] = "B"
        return [y, x, 'right']
    elif getOrientation() == 'left':
        y = random.randint(0,11)
        x = random.randint(5,14) #bones of length 6 overflow if placed less than 5
        for i in range(6, 0, -1):
            yardWithAllBones[y][x - i] = "B"
        return [y, x, 'left']
    elif getOrientation() == 'up':
        y = random.randint(6,11) #bones of length 6 overflow if placed less than 5
        x = random.randint(0,14)
        for i in range(6, 0, -1):
            yardWithAllBones[y - i][x] = "B"
        return [y, x, 'up']
    elif getOrientation() == 'down':
        y = random.randint(0,5) #bones of length 6 overflow if placed greater than 6
        x = random.randint(0,14)
        for i in range(6):
            yardWithAllBones[y + i][x] = "B"
        return [y, x, 'down']

def showYard(desiredYard):
    """
    This function shows either the entire yard with all the locations of the buried bones
    which are randomly determined, or shows the yard with one soecified bone by changing
    the desiredYard parameter.
    """
    top = "" #x axis numbers
    sideNum = 0 #y axis numbers
    #create the x axis numbers
    for i in range(15):
        if i <= 9:
            top += str(i) + "  " #add one space between double digits
        if i > 9:
            top += str(i) + " "  #add two spaces between single digits
    print(top)
    #create the rows of dots and stick the y axis numbers on the ends of them
    for row in desiredYard:
        print("  ".join(row) + "  " + str(sideNum))
        sideNum += 1

def showBone(boneNumber):
    """
    showBone() displayes the location of a single bone which the user defines.
    The way this function works is it temporarily creates another matrix and
    draws the specified bone on to it.  When the function is called again,
    the matrix with the previous bone is overwritten to a blank one in order
    to draw the single new bone.  The first dimension of the 'bones' matrix is
    which bone the user wants, and the second dimension includes the x coordinate,
    y, coordinate, and direction.  This information is put into yardToShowBoneIn.
    """

    #draw the bones
    yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
    if bones[boneNumber-1][2] == 'right':
        for i in range(6):
            yardToShowBoneIn[bones[(boneNumber-1)][0]][bones[(boneNumber-1)][1] + i] = "B"

    elif bones[boneNumber-1][2] == 'left':
        yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
        for i in range(6, 0, -1):
            yardToShowBoneIn[bones[(boneNumber-1)][0]][bones[(boneNumber-1)][1] - i] = "B"

    elif bones[boneNumber-1][2] == 'up':
        yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
        for i in range(6, 0, -1):
            yardToShowBoneIn[bones[(boneNumber-1)][0] - i][bones[(boneNumber-1)][1]] = "B"

    elif bones[boneNumber-1][2] == 'down':
        yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
        for i in range(6):
            yardToShowBoneIn[bones[(boneNumber-1)][0] + i][bones[(boneNumber-1)][1]] = "B"

    showYard(yardToShowBoneIn)


#MAIN
print("""Welcome to Sherlock Holmes' and Toby's Fast Bone Investigation (FBI) app.
This app shows possible patterns in which bones can be buried in Mrs. Hudson's backyard!
These "buried bone" patterns can be used to play the Fast Bone Investigation (FBI) game.\n\n
Here is the backyard with 0 bones buried.""")

#show a blank yard when the program starts
showYard(yardWithAllBones)
#bury each bone and remember where it is by appending y and x coordinates and direction to a list
for i in range(8):
    bones.append(placeBone())
while None in bones:
    bones[bones.index(None)] = placeBone()

#get the valid input with guardian code
running = True
while running:
    choice = input("""\n\nWhere should Sherlock Holmes bury bone x for Toby to find?
Please, enter a bone number from 1 to 8 and this app shall show a location where this bone could be buried.
Enter -1 to quit or 0 to display all bones at once: """)

    if len(choice) == 0:
        print("***You have not entered anything. You need to enter a valid number!")
    elif re.match("^\d+?\.\d+?$", choice) is not None:
        print("***You have entered " + str(choice) + ".  That doesn't make sense.  Please enter an integer.")
    elif len(re.findall("[A-Z]", choice)) >= 1 or len(re.findall("[a-z]", choice)) >= 1:
        print("***You have entered " + str(choice) + ".  You need to enter a valid number!")
    elif int(choice) == -1:
        print("\n-------")
        running = False
    elif int(choice) < -1 or int(choice) > 8:
        print("***You have entered " + str(choice) + " which is not in the desired range. You need to enter a valid number!")
    else:
        choice = int(choice)
        #good to go!
        if choice == 1:
            YardWithOneBoneMsg("1")
            showBone(1)
        elif choice == 2:
            YardWithOneBoneMsg("1")
            showBone(2)
        elif choice == 3:
            YardWithOneBoneMsg("1")
            showBone(3)
        elif choice == 4:
            YardWithOneBoneMsg("1")
            showBone(4)
        elif choice == 5:
            YardWithOneBoneMsg("1")
            showBone(5)
        elif choice == 6:
            YardWithOneBoneMsg("1")
            showBone(6)
        elif choice == 7:
            YardWithOneBoneMsg("1")
            showBone(7)
        elif choice == 8:
            YardWithOneBoneMsg("1")
            showBone(8)
        elif choice == 0:
            YardWithOneBoneMsg("8")
            showYard(yardWithAllBones)
