num = int(input())
check = 0

if num < 100:
    print(num)

else:
    nowNum = num
    check = check + 99
    if num == 1000:
        nowNum = nowNum - 1

    target = list(map(int, str(nowNum)))

    for i in range(100, num):
        target = list(map(int, str(nowNum)))
        if target[0] - target[1] == target[1] - target[2]:
            check = check + 1
        nowNum = nowNum - 1

    print(check)

