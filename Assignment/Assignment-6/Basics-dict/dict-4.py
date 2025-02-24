# 4. Iterating Over a Dictionary
# Write a Python program that iterates over the following dictionary and prints each
# key-value pair:
# fruits = {apple: 10, banana: 5, cherry: 15}

def print_dict(d):
    for x, y in d.items():
        print(x, y)
        
fruits = {"apple": 10, "banana": 5, "cherry": 15}

print_dict(fruits)