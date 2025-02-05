#my_tuple = (4, 8, 12, 16)
#Try modifying the second element of my_tuple to 10. Observe the output and explain why there was
#an error.

def modify_tuple():
    my_typle = (4, 8, 12, 16)
    my_typle[1] = 10
    
    print(my_typle)
    
modify_tuple()

#Once a tuple is created, you cannot change its values.
#Tuples are unchangeable, or immutable as it also is called.