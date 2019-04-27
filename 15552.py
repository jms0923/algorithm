import sys

lineNum = int(sys.stdin.readline())
for i in range(0, lineNum):
    a, b = sys.stdin.readline().split()
    print(int(a) + int(b))
