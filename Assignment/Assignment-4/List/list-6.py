#Find second largest number in a list

def find_second_largest(lst):
    largest = second_largest = float('-inf')
    for num in lst:
        if num > largest:
            largest = second_largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest        

lst = [23,43,53,33,13,24,44]

print(find_second_largest(lst))