#Nested Tuples & Accessing Elements
#Given the nested tuple:
#nested_tuple = ((1, 2, 3), (a, b, c), (True, False))
#Write a Python program to:
#Print the second element of the second inner tuple.
#Extract the last element of the third inner tuple.

def print_second_element(t):
    print(t[1][1])

def print_last_element(t):
    print(t[2][1])
    
t = ((1, 2, 3), ('a', 'b', 'c'), (True, False))
print_second_element(t)
print_last_element(t)
