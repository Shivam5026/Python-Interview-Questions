#2.Write a program to input a 10 digit number and find the digit with maximum value.

def question_2():
    num = int(input("Enter 10 digit number: "))
    max = 0
    while(num>0):
        digit = num % 10
        if(digit > max):
            max = digit
        num = num//10
    print("The max digit is ",max)
    return 0

question_2()