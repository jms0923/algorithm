from collections import deque

def Input():
    kList = []
    originList = list(map(int, input().split()))
    for i in range(originList[2]):
        kList.append(list())
    # print(originList[2])
    for i in range(originList[2]):
        kList[i] = list(map(int, input().split()))

    # print(originList)
    # print(kList)
    reList = [originList]
    # reList.extend(list(originList))
    reList.extend(kList)
    # print('reList', reList)

    return reList

class Node:
    def __init__(self, N, M, next=None):
        self.N = N
        self.M = M
        self.next = next

def main():
    inputList = Input()
    # print('kList\n', inputList)
    nmk = inputList.pop(0)
    maxM = nmk[0]
    maxN = nmk[1]
    numK = nmk[2]
    manyK = [0] * numK
    nowK = 0
    queue = deque()
    nodeList = []

    checkList = [[False] * maxN for i in range(maxM)]

    for i in range(maxN):
        for j in range(maxM):
            nodeList.append(Node(j, i))
    # print('checkList\n', checkList)

    boxList = [[False for i in range(maxN)] for i in range(maxM)]
    for i in range(numK):
        tmpBox = inputList.pop(0)
        minX = tmpBox[0]
        minY = tmpBox[1]
        maxX = tmpBox[2]
        maxY = tmpBox[3]
        for j in range(minY, maxY):
            for k in range(minX, maxX):
                boxList[j][k] = True

    # print('boxList\n', boxList)


    checkNum = 1
    allNodeNum = maxM * maxN
    nowNodeNum = 0
    queue.append(nodeList.pop(0))
    while True:
        if nodeList:
            if queue:
                nowNode = queue.popleft()
                if checkList[nowNode.N][nowNode.M] == False:
                    checkList[nowNode.N][nowNode.M] = True
                    # nowNodeNum += 1
                    if boxList[nowNode.N][nowNode.M] == False:
                        manyK[nowK] += 1
                        queue.append(nodeList[(nowNode.N * maxN) + nowNode.M])
                    else:
                        queue.append(nodeList.pop(0))

                else:
                    # nowNodeNum += 1
                    queue.append(nodeList.pop(0))
            else:
                nowK += 1
                queue.append(nodeList.pop(0))
        else:
            break

    print(nowK, '\n', manyK)


main()
