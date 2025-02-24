#9. Finding Maximum and Minimum Values in a Dictionary
#Given the dictionary:
#scores = {Alice: 85, Bob: 92, Charlie: 78, David: 95}
#Write a Python program to find the student with the highest and lowest scores.

def find_min_max(d):
    max_student = max(d, key=d.get)
    max_score = d[max_student]
    
    min_student = min(d, key=d.get)
    min_score = d[min_student]
    
    print(f"Highest Score: {max_student} ({max_score})")
    print(f"Lowest Score: {min_student} ({min_score})")

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
find_min_max(scores)