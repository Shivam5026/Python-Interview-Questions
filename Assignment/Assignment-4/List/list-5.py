#Remove duplicates from a list

def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

lst = [1, 2, 3, 2, 4, 5, 3, 6]
print("list containing duplicates: ",lst)
print("list after duplicate items removed: ",remove_duplicates(lst))