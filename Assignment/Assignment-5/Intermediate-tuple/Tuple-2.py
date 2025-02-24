#Write a function check_membership(t, element) that takes a tuple t and a value element as input
#and returns True if the element exists in the tuple, otherwise False.

def check_membership(t, element):
    for num in t:
        if(num == element):
            return True
        else: 
            return False

t = (1, 22, 33, 5, 70)
element = 6
print(check_membership(t, element))        