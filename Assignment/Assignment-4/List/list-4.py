#Remove multiple elements from a list

def remove_elements(lst, n):
    for i in range(n):
        lst.pop()
    return lst

lst = [23,43,64,63,66,24,643,364,345,34,4322]
n = 3 #no. of items to remove
print("list before removal: ", lst)
print("list after removal: ", remove_elements(lst,n))