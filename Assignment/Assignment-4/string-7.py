#Replace All Characters Except a Given Character

def replace_except(s, char):
    return "".join(c if c == char else '*' for c in s)

s = input("Enter a string: ")
char = input("Enter the character to keep: ")
print("Modified string:", replace_except(s, char))