def fact(N):
    product = 1
    for i in range(1, N + 1):
        product = product * i
    return product
def nthTerm(N):
    return (N * N) * fact(N)
if __name__ =="__main__":
    N = int(input("Enter an integer: "))
    print(nthTerm(N))