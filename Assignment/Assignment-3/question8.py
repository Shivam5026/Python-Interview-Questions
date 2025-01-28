#8.Write a program to input a number and search in a list using binary search.

def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n-1
    
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = list(map(int, input("Enter number in the list separated with spaces: ").split()))
target = int(input("Enter the number to search: "))
result = binary_search(arr, target)
if result != -1:
    print(f"The Number {target} is found at index {result}.")
else:
    print(f"The Number {target} is not found.")        