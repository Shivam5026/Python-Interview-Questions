#Write a Python program that packs the values ("Alice", 25, "Engineer") into a tuple and then unpack
#them into separate variables.

def unpack_tuple():
    employee = ("Alice", 25, "Engineer")
    
    name, age, job = employee
    
    print(name, age, job)

unpack_tuple()