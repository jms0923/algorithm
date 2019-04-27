import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().rstrip().replace('[', '', 1).replace(']', '', 1).split(', ')))
arr2 = list(map(int, sys.stdin.readline().rstrip().replace('[', '', 1).replace(']', '', 1).split(', ')))
mapped = []

for i in range(len(arr1)):
    mapped.append(bin(arr1[i] | arr2[i])[2:].zfill(n))

for i in range(len(arr1)):
    mapped[i] = mapped[i].replace('1', '#').replace('0', ' ')

for i in mapped:
    for j in range(len(i)):
        if j == '1':
            print()

print(mapped)

print(bin(19))
print(bin(33))
print(bin(56))
