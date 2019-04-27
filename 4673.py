def CalSelfNum(mainNum):
    splitedMainNum = list(map(int, (list(str(mainNum)))))

    combineNum = mainNum
    for i in splitedMainNum:
        combineNum += i

    return combineNum

def main():
    mainNum = 1
    selfNumList = []

    for i in range(1, 9999):
        mainNum = i
        while mainNum < 10000:
            mainNum = CalSelfNum(mainNum)
            if mainNum in selfNumList:
                selfNumList.insert(-1, mainNum)

    sortedList = list(set(selfNumList))
    # print(sortedList)
    for i in range(1, 10000):
        if i not in sortedList:
            print(i)


main()