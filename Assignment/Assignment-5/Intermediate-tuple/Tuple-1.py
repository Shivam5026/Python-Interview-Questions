#Tuple Concatenation &amp; Repetition
#Given two tuples:
#t1 = (1, 2, 3)
#t2 = ('a', 'b, 'c')
#Write a Python program to concatenate t1 and t2, then repeat the resulting tuple 2 times.

def concatenate():
    t1 = (1, 2, 3)
    t2 = ('a', 'b', 'c')
    
    t3 = t1 + t2
    
    t4 = t3 * 2
    
    print(t4)
    
concatenate()