import sys

caseNum = int(input())

for i in range(caseNum):
    docNum, targetDocNum = map(int, sys.stdin.readline().split())
    printQue = list(map(int, sys.stdin.readline().split()))

    printedNum = 0                                  # 뽑힌 문서 수
    # endPoint = True                               # False 면 종료

    while True:
        priority = False                            # 우선 순위가 높은게 있나?
        nowPrinted = printQue.pop(0)                # 일단 한놈 뽑아서
        for j in printQue:                          # 중요도 검사
            if nowPrinted < j:
                priority = True                     # 우선순위 높은게 있음
                break

        if not priority:                            # 뽑기 O
            if targetDocNum == 0:                   # 근데 그게 타겟 문서인 경우
                print(printedNum + 1)
                break

            else:                                   # 타겟 문서가 아닌 경우
                printedNum = printedNum + 1         # 뽑은 문서 수  + 1
                targetDocNum = targetDocNum - 1     # 타겟 문서 위치 - 1

        else:                                       # 뽑기 X
            printQue.append(nowPrinted)             # 맨 뒤에다가 추가

            if targetDocNum == 0:                   # 근데 그게 타겟 문서 0
                targetDocNum = len(printQue) - 1

            else:                                  # 근데 그게 타겟 문서 X
                targetDocNum = targetDocNum - 1
