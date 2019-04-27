import sys

a = int(sys.stdin.readline().rstrip(), 2)
b = int(sys.stdin.readline().rstrip(), 2)
print(bin(a & b)[2:].zfill(100000))
print(bin(a | b)[2:].zfill(100000))
print(bin(a ^ b)[2:].zfill(100000))
print(bin(a)[2:].zfill(100000).replace('0', '2').replace('1', '0').replace('2', '1'))
print(bin(b)[2:].zfill(100000).replace('0', '2').replace('1', '0').replace('2', '1'))

