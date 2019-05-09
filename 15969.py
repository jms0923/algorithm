studentNum = int(input())
studentList = list(map(int, input().split()))

maxPoint = max(studentList)
minPoint = min(studentList)

print(maxPoint - minPoint)

