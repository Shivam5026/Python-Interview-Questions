# 13.Write a program to input a string and a number to encode the string by adding the number to 
# every character in the string

def encode_string(string, shift):
    encode_string = ""
    for char in string:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - base + shift) % + base)
        else:
            encoded_char = char
            encode_string += encoded_char
    return encode_string

string = input("Enter the string to encode: ")
shift = int(input("Enter the number to shift by: "))

encoded = encode_string(string, shift)

print("Encoded String:", encoded)