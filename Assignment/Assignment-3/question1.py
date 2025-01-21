#1.Write a program to input a 4 digit number and print the even and odd digits and total even and
#odd digits

def question_1():
    n = int(input("Enter the number: "))
    evenNumber = []
    oddNumber = []
    while (n>0):
        digit = n % 10
        if(digit % 2 == 0):
            evenNumber.append(digit) 
        else:
            oddNumber.append(digit) 
        n = n//10
    
    print("The even numbers are: ")
    for i in evenNumber:
        print(i)
    
    print("The odd number are: ")    
    for i in oddNumber:
        print(i)    
    
    print("Total even numbers: ")
    print(len(evenNumber))
    
    "Total odd numbers: "
    print(len(oddNumber))
    return 0

question_1()