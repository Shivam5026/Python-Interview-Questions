def findNth(N):
    b = 14
    for i in range (2, N + 1):
        if (i % 2 == 0):
            b = b * 2
        else:
            b = b - 8
    return b
N = int(input("Enter an integer: "))
print(findNth(N))