#write a pyhton program to interchange the first and last digit of a list
#write a program in pyhton that take an array and split two halves and add first with the second array

def interchange(lst):

    if len(lst) > 1 :
        lst[0], lst[-1] = lst[-1], lst[0]
    else: 
        return None
    
lst = list(map(int, input("Enter a list of number separated by spaces:").split()))

interchange(lst)

print(lst)


def split_and_add(arr):
    mid = len(arr)//2
    
    first_half = arr[:mid]
    second_half = arr[mid:]
    
    if len(first_half) != len(second_half):
        second_half.append(0)
        
    result = [second_half[i] + first_half[i] for i in range(len(first_half))]
    
    return result

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

print(split_and_add(arr))