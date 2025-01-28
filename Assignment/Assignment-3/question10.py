#10.Write a program to input a list of numbers and sort using insertion sort.

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1]   = key
        
arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

insertion_sort(arr)

print("sorted list: ", arr)