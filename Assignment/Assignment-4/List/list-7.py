#Intersection of two lists

def intersection_of_two_lists(lst1, lst2):
    intersection = [item for item in lst1 if item in lst2]
    return intersection

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

print("Intersections of the two lists: ", intersection_of_two_lists(lst1,lst2))