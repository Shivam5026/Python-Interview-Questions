#6.Given a sorted array of positive integers arr, and an integer n which represents the length of arr,
#the task is to rearrange the array elements alternatively i.e first element should be max value,
#second should be min value, third should be second max, fourth should be second min and so on.

def question_6(sorted_arr, n):
    resul_arr = [0] * n
    max_index = n-1
    min_index = 0
    
    flag = True
    
    for i in range(n):
        if flag:
            resul_arr[i] = sorted_arr[max_index]
            max_index -= 1
        else:
            resul_arr[i] = sorted_arr[min_index]
            min_index += 1
        flag = not flag
    print("Rearranged array:", resul_arr)

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
question_6(arr,n)        