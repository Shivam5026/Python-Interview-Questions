#12.Write a program to find the frequency of characters in a given string.

def character_frequency(string):
    # Dictionary to store the frequency of characters
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Input string
string = input("Enter a string: ")

frequencies = character_frequency(string)

print("Character Frequencies:")
for char, count in frequencies.items():
    print(f"'{char}' : {count}")    