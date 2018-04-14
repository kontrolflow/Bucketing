#!/usr/bin/env python3

print("Hello World")

# Bucketing
#Jullian and I use python to basically build the bucket sort algorithm (or attempt to.... we kinda know what we're doing, ha.)

#example array (working with single digits for now)
array = [1,5,4,6]

#we create empty an empty list
bucket = []

#We make an empty dictionary
bucket2 = {}


#We set up a for loop to iterate all the elements "tagging" them into place.
for n in array:
    bucket2[n] = n

#Print the sorted list
print(bucket2.values())