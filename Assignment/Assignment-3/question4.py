#4.Write a program, which will find all such numbers between 1000 and 3000 such that each digit of
#the number is an even number.

def question_4():
    result = []
    
    for num in range(1001, 3000):
        num_str = str(num)
        if all (int(digit)%2==0 for digit in num_str):
            result.append(num)
    print("Numbers where all digits are even:")
    print(result)               
question_4()
        