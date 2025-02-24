#Count occurences of elements in a list

def count_occurences(lst, element):
    n = len(lst)
    count = 0
    for i in range(n):
        if lst[i] == element:
            count+=1
    print(f"{element} occured {count} times")        
    
lst = [23, 35, 54, 53, 23, 23]
count_occurences(lst,23)