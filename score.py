def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = float(score1)
    score2 = float(score2)
    score3 = float(score3)
    score4 = float(score4)
    score5 = float(score5)

    #STEP 2 find middle three scores
    sum_of_middle=sum_of_middle_three(score1,score2,score3,score4,score5)

    #STEP 3 take average of middle three scores
    average_score = sum_of_middle/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating


def sum_of_middle_three(score1,score2,score3,score4,score5):
    min_score=min(score1,score2,score3,score4,score5)
    max_score=max(score1,score2,score3,score4,score5)
    sum_of_middle=score1+score2+score3+score4+score5-min_score-max_score
    return sum_of_middle

def score_to_rating_string(score):
    if 0 <= score < 1:
        return "Terrible"
    elif 1 <= score < 2:
        return "Bad"
    elif 2 <= score < 3:
        return "OK"
    elif 3 <= score < 4:
        return "Good"
    elif 4 <= score <= 5:
        return "Excellent"
    else:
        return "Unknown"

print(scores_to_rating(1,2,3,4,5))
