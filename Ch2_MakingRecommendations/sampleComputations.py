__author__ = 'sharmrav'

from math import  sqrt

#Euclidean Distance Computation . Subtracting coordinates square them, add them and then take sqrt
val = sqrt(pow(5-4,2)+pow(4-1,2))
print(val)

#to get val between 0 and 1 ( and get higher values for higher similarities)
print(1/(1+val))