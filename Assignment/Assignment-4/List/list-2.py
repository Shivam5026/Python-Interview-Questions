#Cloning or copying a list

def cloning_list(lst):
    mylist = lst.copy()
    print("The original list: ", lst)
    print("The cloned list: ", mylist)

n = int(input("Enter the no. of Elements: "))

thelist = []

for i in range(n):
    item = input(f"Enter item {i+1}: ")
    thelist.append(item)

cloning_list(thelist)