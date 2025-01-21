def findNthTerm(n):
    if (n % 2 == 0):
        n = n // 2
        n = 2 * (n - 1)
        print( n // 2)
    else:
        n = (n // 2) + 1
        n = 2 * (n - 1)
        print(n)
if __name__ == "__main__":
    X = int(input("enter an integer: "))
    findNthTerm(X)