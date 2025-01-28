#Write a program that prints a list where the values are square of numbers between 5000 and
#7000 (both included).

def question_5():
    squares = []
    for num in range(5000, 7001):
        square = num ** 2
        squares.append(square)
    print("Square of numbers between 5000 and 7000:")
    print(squares)    
question_5()        