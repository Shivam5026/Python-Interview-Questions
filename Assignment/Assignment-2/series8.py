def nthTerm(N) :
    return (abs(N * ((N - 1) * (N - 3) * (N - 5))))
if __name__ == "__main__" :
    N = int(input("Enter an integer: "))
    print(nthTerm(N))