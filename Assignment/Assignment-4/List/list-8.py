#Check if two lists are identical

def identical(lst1, lst2):
    return lst1 == lst2
 

lst1 = [1,2,3,4]
lst2 = [1,2,3]    

if identical(lst1,lst2):
    print("Identical Lists.")
else: print("Not Identical Lists.")