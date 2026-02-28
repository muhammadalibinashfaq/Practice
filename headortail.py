import random

countHead=0
countTail=0
for i in range(0,100):
    toss = random.choice(["head", 'tail'])

    if toss=='head':
        countHead+=1
    else:
        countTail+=1
print(countHead)
print(countTail)