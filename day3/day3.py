#!/usr/bin/env python3
print('Hello World!')
from string import ascii_lowercase
from string import ascii_uppercase

priority=1
priorities={}
for c in ascii_lowercase:
    priorities[c]=priority
    priority+=1
for C in ascii_uppercase:
    priorities[C]=priority
    priority+=1
    # append to your url
f = open("input.txt","r")
lines = f.readlines()
sum=0
for line in lines:
    sanitizedline=line.replace("\n","")
    part1=sanitizedline[0:int(len(sanitizedline)/2)] 
    part2=sanitizedline[int(len(sanitizedline)/2):int(len(sanitizedline))]
    previoussum=sum;
    for a in part1:
        if previoussum!=sum:
            break
        for b in part2:
            if a==b:
                print("Found match: " + a)
                sum+=priorities[a]
                break
print(sum)
