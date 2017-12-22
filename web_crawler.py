#search_history is a list of strings which are the urls of Wikipedia articles. The last item in the list most recently found url.
#target_url is a string, the url of the article that the search should stop at if it is found.
#continue_crawlshould return True or False following these rules:

#if the most recent article in the search_history is the target article the search should stop and the function should return False
#If the list is more than 25 urls long, the function should return False
#If the list has a cycle in it, the function should return False
#otherwise the search should continue and the function should return True.
#For this quiz, implement continue_crawl. For each of the situations where the search stops, print a message that briefly explains why. Remember to test your code!


# TODO: Implement the continue_crawl function described above

def continue_crawl(search_history, target_url):
    if  (search_history[-1] == target_url) | (len(search_history) > 25) | (target_url in search_history) | (len(search_history) !=len(set(search_history))):
        return False
    else:
        return True

print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],
                       'https://en.wikipedia.org/wiki/Philosophy'))



#Udacity solution
def continue_crawl(search_history, target_url):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > 25:
        print("The search has gone on suspiciously long; aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen; aborting search!")
        return False
    else:
        return True
