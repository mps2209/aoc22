#!/usr/bin/env python3
import numpy as np

print('Hello World!')

f = open("input.txt","r")
lines = f.readlines()
sum=0
for line in lines:
    sanitizedline=line.replace("\n","")
    sections=sanitizedline.split(",")
    rangeA=list(range(int(sections[0].split("-")[0]),int(sections[0].split("-")[1])+1))
    
    rangeB=list(range(int(sections[1].split("-")[0]),int(sections[1].split("-")[1])+1))
    print(sanitizedline)
    print(rangeA)
    print(rangeA[0])
    print(rangeA[len(rangeA)-1])
    print(rangeB)
    print(rangeB[0])
    print(rangeB[len(rangeB)-1])
    if rangeA[0] in rangeB or rangeB[0] in rangeA or rangeA[len(rangeA)-1] in rangeB or rangeB[len(rangeB)-1] in rangeA:
        sum+=1
print(sum)

