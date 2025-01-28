#7.Write a program to input a number and search in a list using linear search.

def linear_search(arr, target):
    n = len(arr)    
    for i in range(n):
        if(arr[i] == target):
            return i
    return -1        

# Input the List of Numbers
arr = list(map(int, input("Enter numbers in the list separated by space: ").split()))

# Input the Target number to search
target = int(input("Enter the number to Search: "))

result = linear_search(arr, target)

# Display the result
if result != -1:
    print(f"Number {target} is found at index {result}.")
else:
    print(f"Number {target} is not found in the List.")