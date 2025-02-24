#1. Dictionary Creation &amp; Accessing Values
#Create a dictionary student with the following key-value pairs:
#{
#name:John,
#age: 20,
#course: Computer Science
#}
#Write a Python program to print the students name and course.

def get_student_detail():
    student_dict = {
        "name" : "john",
        "age" : 20,
        "course" :"Computer Science"
    }
    
    print(student_dict["name"], student_dict["course"])
    
get_student_detail()