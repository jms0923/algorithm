a, b, c, n = input().split()
a, b, c, n = int(a), int(b), int(c), int(n)
end = 0


for i in range(1, 301):
    for j in range(1, 301):
        for k in range(1, 301):
            if a*i + b*j + c*k == n:
                end = 1
                break

            if a*i == n or b*j == n or c*k == n:
                end = 1
                break

            if b*j + c*k == n or a*i + c*k == n or a*i + b*j == n:
                end = 1
                break

        if end == 1:
            break

    if end == 1:
        break


print(end)

