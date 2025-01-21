import math
def findNthTerm(n):
    n = n * 2
    a = 1
    b = 1
    c = -1 * n
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))
    x1 = (-b + sqrt_val) // (2 * a)
    x2 = (-b - sqrt_val) // (2 * a)
    x1 = int(x1)
    x2 = int(x2)
    if (x1 >= 1):
        print(chr(97+x1))
    elif (x2 >= 1):
        print(chr(97+x2))
if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    findNthTerm(n)