def printNthElement(n) :
    arr =[0] * (n + 1)
    arr[1] = 3
    arr[2] = 5
    for i in range(3, n + 1) :
        if (i % 2 != 0) :
            arr[i] = arr[i // 2] * 10 + 3
        else :
            arr[i] = arr[(i // 2) - 1] * 10 + 5
    return arr[n]

n = int(input("Enter the number: "))
print(printNthElement(n))