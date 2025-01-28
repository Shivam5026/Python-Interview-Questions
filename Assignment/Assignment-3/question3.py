#3.Write a program to input a 10 digit number and print alternate digits.

def question_3():
    num = input("Enter a 10 digit number: ")
    n = len(num)
    if(n!=10 or not num.isdigit()):
        print("Please enter a valid 10-digit number.")
        return
    for i in range(0,n,2):
        print(num[i], end=" ")
    return 0

question_3()