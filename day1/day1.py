#!/usr/bin/env python3
print('Hello World!')
f = open("calories.txt","r")
lines = f.readlines()
elfescount=0
elfesCalories=[0]

for line in lines:
    if line=="\n":
        print("next elfe")
        print(elfesCalories[elfescount])
        elfesCalories.append(0)
        elfescount+=1
    else:
        print(line)
        elfesCalories[elfescount]+=int(line)
highestCalories=0
for elfe in elfesCalories:
    print(elfe)
    if elfe > highestCalories:
        highestCalories=elfe
print(highestCalories)

