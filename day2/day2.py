#!/usr/bin/env python3
print('Hello World!')
RPS={
    "X":1,
    "Y":2,
    "Z":3
}
RPSScore={
    "A":{
        "X":4,
        "Y":8,
        "Z":3
    },
    "B":{
        "X":1,
        "Y":5,
        "Z":9
    },    
    "C":{
        "X":7,
        "Y":2,
        "Z":6
    },
}
RPSStrategy={
    "A":{
        "X":"Z",
        "Y":"X",
        "Z":"Y"
    },
    "B":{
        "X":"X",
        "Y":"Y",
        "Z":"Z"
    },    
    "C":{
        "X":"Y",
        "Y":"Z",
        "Z":"X"
    },
}
f = open("RPS.txt","r")
lines = f.readlines()
totalscore=0
for line in lines:
    sanitizedLine=line.replace("\n", "")
    game=sanitizedLine.split(" ")
    print(game[0])
    print(game[1])
    score=RPSScore[game[0]][RPSStrategy[game[0]][game[1]]]
    print(score)
    totalscore+=score
print(totalscore)

