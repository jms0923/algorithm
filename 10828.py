import sys

lineNum = int(sys.stdin.readline())
stack = []
for i in range(0, lineNum):
    cmd = sys.stdin.readline().rstrip()

    if 'push' in cmd:
        pushNum = int(cmd.split()[1])
        stack.append(pushNum)

    elif 'pop' in cmd:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif 'size' in cmd:
        print(len(stack))

    elif 'empty' in cmd:
        if stack:
            print(0)
        else:
            print(1)

    else:   # top
        if stack:
            print(stack[-1])
        else:
            print(-1)
