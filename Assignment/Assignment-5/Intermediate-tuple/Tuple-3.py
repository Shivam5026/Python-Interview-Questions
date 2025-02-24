# Converting a Tuple to a List and Vice Versa
# Write a Python program that converts the tuple (10, 20, 30, 40, 50) into a list, modifies the second
# element to 25, and then converts it back to a tuple.

def modify_tuple(t, element, value):
    lst = list(t)
    
    lst[element] = value
    
    print(tuple(lst))
    

t = (10, 20, 30, 40, 50)
element = 1
value = 25

print("Tuple before modified: ", t)
print("Tuple after modified:")
modify_tuple(t, element, value)