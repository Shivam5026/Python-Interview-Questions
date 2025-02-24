#Removing all duplicates from a string

def remove_duplicates(str):
    return "".join(sorted(set(str),key=str.index))

str = input("Enter a string: ")
print("String after removing duplicates: ", remove_duplicates(str))