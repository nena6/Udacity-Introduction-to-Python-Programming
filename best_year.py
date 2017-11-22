#Write a function most_prolific that takes a dict formatted like Beatles_Discography example above and returns the year in which the most albums were released. If you call the function on the Beatles_Discography it should return 1964, which saw more releases than any other year in the discography.

#If there are multiple years with the same maximum number of releases, the function should return a list of years.

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1965 ,'Abbey Road': 1969,
    "Let It Be": 1970}

def most_prolific(discography):
    years={}
    all_years=[]
    best_years=[]
    for album in discography:
        if discography[album] in years:
            years[discography[album]]+=1
        else:
            years[discography[album]]=1
    print(years)
    max_year=0
    max_occurence=0
    for year in years:
        if years[year]>max_occurence:
            max_year=year
            max_occurence=years[year]

    return max_year


print(most_prolific(Beatles_Discography))

#Udacity solution

def most_prolific(discs):
#We will store a dictionary of years
#and number of albums per year
    years = {}
    maxyears = []
    maxnumber = 0
    for disc in discs:
        year = discs[disc]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

#find the year in which the maximum
#number of albums was published
#there are more elegant ways of accomplishing this,
#but the code below works
    for year in years:
        if years[year] > maxnumber:
            maxyears=[]
            maxyears.append(year)
            maxnumber = years[year]
        elif years[year] == maxnumber and not (year in maxyears):
            maxyears.append(year)
    if (len(maxyears) == 1):
        return maxyears[0]
    else:
        return maxyears
