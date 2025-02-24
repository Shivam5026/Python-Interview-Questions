#Remove ith Character from the String

def remove_ith_character(s, i):
    if i < 0 or i >= len(s):
        return "Invalid index"
    return s[:i] + s[i+1:]

s = input("Enter a string: ")
i = int(input("Enter index to remove: "))
print("String after removal:", remove_ith_character(s,i))