#Check Whether a String is Symmetrical or Palindrome
def check_symmetrical_palindrome(s):
    mid = len(s) // 2
    if s == s[::-1]:
        print("The string is a palindrome.")
    elif s[:mid] == s[-mid:]:
        print("The string is symmetrical.")
    else:
        print("The string is neither symmetrical nor a palindrome.")
    
s = input("Enter a string: ")
check_symmetrical_palindrome(s)