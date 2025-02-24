#6. Merging Two Dictionaries
#Given two dictionaries:
#d1 = {a: 1, b: 2}
#d2 = {b: 3, c: 4}
#Write a program to merge d1 and d2, where keys in both dictionaries should have the
#values from d2.

def merge_dict(d1, d2):
    d1.update(d2)
    print("Merged Dictionary:",d1)
    
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merge_dict(d1,d2)