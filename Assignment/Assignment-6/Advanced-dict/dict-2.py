#10. Nested Dictionary  Accessing Elements
#Given the dictionary:
#students = {
#   "John": {age: 20, grades: [85, 90, 92]},
#   "Emma": {age: 22, grades: [88, 79, 95]}
#}
# Write a program to:
# Print John age.
# Print Emma highest grade.

students = {
   "John": {"age": 20, "grades": [85, 90, 92]},
   "Emma": {"age": 22, "grades": [88, 79, 95]}
}

jhon_age = students["John"]["age"]
print(f"John's age: {jhon_age}")

emma_highest_grade = max(students["Emma"]["grades"])
print(f"Emma's Highest Grade: {emma_highest_grade}")