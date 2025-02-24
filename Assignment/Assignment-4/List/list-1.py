#Interchange first and last elements in a list

def interchange(lst):
    n = len(lst)
    temp = lst[0]
    lst[0] = lst[n-1]
    lst[n-1] = temp
    return lst

lst = ["apple", "banana", "cherry"]
print("list before interchange: ", lst)
print("list after interchange: ", interchange(lst))