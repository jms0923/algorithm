import sys

numOfBall = int(input())
total = 0
ballList = []
totalByColorList = [0] * (numOfBall + 1)
score = [0] * numOfBall

for i in range(numOfBall):
    a = list(map(int, sys.stdin.readline().split()))
    ballList.append(a)
    ballList[i].append(i)

ballList.sort(key=lambda x: x[1], reverse=False)

j = 0

for i in range(0, numOfBall):
    while True:
        if ballList[j][1] < ballList[i][1]:
            total += ballList[j][1]
            totalByColorList[ballList[j][0]] += ballList[j][1]
            j += 1
        else:
            break
    score[ballList[i][2]] = (total - totalByColorList[ballList[i][0]])

for i in range(0, numOfBall):
    print(score[i])
