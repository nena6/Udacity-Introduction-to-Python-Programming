#The starbox function in the quiz below prints a box made out of asterisks. The function takes two arguments, width and
#height, that specify how many characters wide the box is and how many lines tall it is. The function isn't quite complete: it
#prints boxes of the correct width, but the height argument is ignored. Complete the function so that both of the provided
#test cases print boxes that are the correct size. Hint: The range function could be helpful!

def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box

    # print sides of box
    # todo: print this line height-2 times, instead of three times
    for i in range(height-2):
        print("*" + " " * (width-2) + "*")
    #print("*" + " " * (width-2) + "*")
    #print("*" + " " * (width-2) + "*")

    print("*" * width) #print bottom edge of box

# Test Cases
print("Test 1:")
starbox(5, 5) # this prints correctly

print("Test 2:")
starbox(2, 3)  # this currently prints two lines too tall - fix it!

#Udacity solution

def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box

    # print sides of box
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*")

    print("*" * width) #print bottom edge of box
