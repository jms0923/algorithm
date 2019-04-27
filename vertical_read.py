# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

line_01 = list(input())
line_02 = list(input())
line_03 = list(input())
line_04 = list(input())
line_05 = list(input())

output = ''

for i in range(15):
    if line_01:
        output = output + line_01.pop(0)

    if line_02:
        output = output + line_02.pop(0)

    if line_03:
        output = output + line_03.pop(0)

    if line_04:
        output = output + line_04.pop(0)

    if line_05:
        output = output + line_05.pop(0)

print(output)

