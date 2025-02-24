#Returning Multiple Values from a Function using Tuples

#Write a function math_operations(a, b) that takes two numbers as input and returns a tuple
#containing their sum, difference, product, and quotient.

def math_operations(a, b):
    sum = a+b
    diff = a-b
    prod = a*b
    quotient = a//b
    
    t = (sum, diff, prod, quotient)    

    return t

print(math_operations(4,2))