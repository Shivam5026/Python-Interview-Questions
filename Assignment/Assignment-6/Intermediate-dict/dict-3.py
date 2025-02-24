#8. Converting Two Lists into a Dictionary
#Given two lists:
#keys = [name, age, city]
#values = [Alice, 25, New York]
#Write a program to convert them into a dictionary.

def convert_list_to_dict(keys, values):
    thisdict = dict(zip(keys, values)) 
    print(thisdict)  

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

convert_list_to_dict(keys, values)