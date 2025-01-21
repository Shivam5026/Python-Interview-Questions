def nthTerm(N) :
    return N * N + (N + 1) * (N + 1)
if __name__ == "__main__" :
    N = int(input("Enter an integer: "))    
    print(nthTerm(N))