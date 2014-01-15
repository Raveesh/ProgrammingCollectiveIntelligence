__author__ = 'sharmrav'

# A dictionary of movie critics and their ratings of a small set of movies
from math import sqrt
#dictionary of preferences
critics={'Lisa Rose' : {'Lady in the water' : 2.5, 'Snakes on a Plane' : 3.5, 'Just My Luck' : 3.0, 'Superman Returns' : 3.5 , 'You Me and Dupree' :2.5, 'The Night Listener' :3.0},
         'Gene Seymour' : {'Lady in the water' : 3.0, 'Snakes on a Plane' : 3.5, 'Just My Luck' : 1.5, 'Superman Returns' : 5.0 , 'You Me and Dupree' :3.5, 'The Night Listener' :3.0},
         'Michael Phillips' : {'Lady in the water' : 2.5, 'Snakes on a Plane' : 3.0, 'Superman Returns' : 3.5 , 'The Night Listener' :4.0},
         'Claudia Puig' : {'Snakes on a Plane' : 3.5, 'Just My Luck' : 3.0, 'Superman Returns' : 4.0 , 'You Me and Dupree' :2.5, 'The Night Listener' :4.5},
         'Mick Lasalle' : {'Lady in the water' : 3.0, 'Snakes on a Plane' : 4.0, 'Just My Luck' : 2.0, 'Superman Returns' : 3.0 , 'You Me and Dupree' :2.0, 'The Night Listener' :3.0},
         'Jack Matthews' : {'Lady in the water' : 2.5, 'Snakes on a Plane' : 4.0, 'Superman Returns' : 5.0 , 'You Me and Dupree' :3.5, 'The Night Listener' :3.0},
         'Toby' : {'Snakes on a Plane' : 4.5, 'Superman Returns' : 4.0 , 'You Me and Dupree' :1.5}
         }

#computing similarities based on preferences and the users.
def sim_distance(prefs,person1,person2):
    #Obtain the list of shared items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    #if they have no ratings in common return 0
    if(len(si)) == 0: return 0

    #Add the squares of all differences
    sum_of_squares=sum([pow(prefs[person1][item] - prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    return  1/(1+sum_of_squares)


#this function returns a value between -1 and 1 where 1 means both the users have exactly same ratings for every item

def sim_pearson(prefs,p1,p2):
    #Get the list of manually rated items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:si[item]=1

    #Find the number of elements
    n=len(si)

    #if there are no ratings in common return 0
    if n==0:return 0

    #Add all the preferences
    sum1=sum([prefs[p1][it] for it in si])
    sum2 =sum([prefs[p2][it] for it in si])

    #SUm up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    #Sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    #Calculate Pearson score
    num=pSum - (sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den
    return r


#Return the best matches for the person from the prefs dictionary
def toppMatches(prefs,person,n=5,similarity=sim_pearson):
    scores =[(similarity(prefs,person,other), other) for other in prefs if other!=person]

    #Sort list in descending order to highest score first
    scores.sort()
    scores.reverse()
    return scores[0:n]


