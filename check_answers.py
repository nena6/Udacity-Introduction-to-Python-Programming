def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    my_answers: list
        List of answers
    answers: list
        List of correct answers
    """


    count = 0;
    for i in range(len(answers)):
        if my_answers[i]==answers[i]:
            count+=1
        i+=1

    if count/(len(answers)) > 0.7:
        return ("Congratulations, you passed the test! You scored " + str(count) + " out of " + str(len(answers)) + ".")
    else:
        return ("Unfortunately, you did not pass. You scored " + str(count) + " out of " + str(len(answers)) + ".")



results= [1, 2, 8, 4, 5]
answers= [1, 2, 3, 4, 5]

print(check_answers(answers, results))

#Udacity solution

def check_answer(my_answer, answer):
    if my_answer == answer:
        return True
    else:
        return False

def check_answers(my_answers,answers):
    #Checks the five answers provided to a multiple choice quiz and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test!"
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass."
