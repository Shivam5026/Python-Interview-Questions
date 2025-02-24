#Maximum and minimum element’s position in a list

def max_min_ele_pos(lst):
    
    max_value = max(lst)
    min_value = min(lst)
    
    max_pos = lst.index(max_value)
    min_pos = lst.index(min_value)
    
    print(f"Maximum value {max_value} is at position {max_pos}.")
    print(f"Maximum value {min_value} is at position {min_pos}.")
    

lst = [10, 20, 4, 45, 99, 45]
max_min_ele_pos(lst)