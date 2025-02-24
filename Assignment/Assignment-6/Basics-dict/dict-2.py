#2. Adding and Updating Dictionary Elements
# Given the dictionary:
# employee = {name:Alice, salary: 5000}
# Add a new key department with the value HR.
# Update salary to 5500.
# Print the updated dictionary.

def add_and_update_dict():
    employee = {
        "name" : "Alice",
        "salary" : 5000
    }
    x = employee.items()
    print("Dictionary before: ",x)     
    employee.update({"department":"HR"})
    employee.update({"salary":5500})
    print("Dictionary after: ", x)
add_and_update_dict()