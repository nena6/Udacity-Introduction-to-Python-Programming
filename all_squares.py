#In a similar way to building an empty list with my_list = [], you can create an empty set with my_set = set(). Using this technique, and the add method, build a set of all of the square numbers greater than 0 and less than 2,000. For reference, I included my implementation of nearest_square function from an earlier quiz. You may call the function in your code, integrate it into your code, or ignore it altogether.

def all_squares(limit):
    squares_set=set()
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
        squares_set.add(answer**2)
    return squares_set


print(all_squares(2000))

#Udacity solution

n = 1
while n**2 < 2000:
    squares.add(n**2)
    n += 1

#It was tempting to simply use the nearest_square function as originally written by calling it repeatedly in a loop, but I realized that this would cause my computer to do the same calculations repeatedly. For example, if the loop called nearest_square(1999) and then nearest_square(2000),it would have to iterate from 1 to 1,999 all over again to produce a result.
