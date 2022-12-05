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
i=0
numpacks=0
packs={
    0:[]
}
for line in lines:

    sanitizedline=line.replace("\n","")
    packs[numpacks].append(sanitizedline)
    if i==2:
        numpacks+=1
        i=0
        packs[numpacks]=[]
    else:
        i+=1
sum=0
for pack in packs:
    if packs[pack]==[]: 
        break
    holepack=""
    print(packs[pack])
    for c in packs[pack][0]:
        if(c in packs[pack][1] and c in packs[pack][2]):
            sum+=priorities[c]
            break
print(sum)
        


