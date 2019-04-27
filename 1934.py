def lcm(a, b):      # least common multiple 최소공배수
    gcm = 1

    for k in range(2, min(a, b) + 1):
        while (a % k == 0) and (b % k == 0):
            a = a // k
            b = b // k
            gcm = gcm * k

    lcm = gcm * a * b

    return lcm


if __name__ == '__main__':
    testCaseNum = int(input())

    for _ in range(testCaseNum):
        m, n = map(int, input().split())
        print(lcm(m, n))
