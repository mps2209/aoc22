#!/usr/bin/env python3
print('Hello World!')

f = open("input.txt","r")
lines = f.readlines()
sum=0
for line in lines:
    sanitizedline=line.replace("\n","")
    sections=sanitizedline.split(",")
    sections[0]=sections[0].split("-")
    sections[1]=sections[1].split("-")
    if int(sections[0][0])>=int(sections[1][0]) and int(sections[0][1])<=int(sections[1][1]):
            print(sanitizedline)
            sum+=1
    else: 
        if int(sections[0][0])<=int(sections[1][0])and int(sections[0][1])>=int(sections[1][1]):
            print(sanitizedline)
            sum+=1

print(sum)
