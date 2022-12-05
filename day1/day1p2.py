#!/usr/bin/env python3
print('Hello World!')
f = open("../day1/calories.txt","r")
lines = f.readlines()
elfescount=0
elfesCalories=[0]

for line in lines:
    if line=="\n":
        elfesCalories.append(0)
        elfescount+=1
    else:
        elfesCalories[elfescount]+=int(line)
highestCalories=0
elfesCalories.sort(reverse=True)
print(elfesCalories[0]+elfesCalories[1]+elfesCalories[2])