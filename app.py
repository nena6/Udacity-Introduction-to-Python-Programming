#Let's revisit the survey information from earlier. Before we used a set to determine how many unique countries were in the dataset. Suppose this dataset actually contains information about users who downloaded and installed a certain application: for each user that did this their country appears in the list. Now let's use a dict to perform a more sophisticated analysis: how many users there are from each country?

#Create a dict, country_counts whose keys are country names, and whose values are the number of times the country occurs in the countries list. Write your code in the app.py file.

from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country not in country_counts:
        country_counts[country] = 1
    else:
        country_counts[country]+=1

print(country_counts)

#Udacity solution
