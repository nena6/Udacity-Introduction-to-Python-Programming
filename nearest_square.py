#Implement the nearest_square function. The function takes an integer argument limit, and returns the largest square number that is less than limit. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

#There's more than one way to write this code, but I suggest you use a while loop!

#TODO: Implement the nearest_square function

def nearest_square(limit):
    x=0
    square=0
    while ((x*x)<limit):
        square=x*x
        x+=1
    return square

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))



#Udacity solution

def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2
