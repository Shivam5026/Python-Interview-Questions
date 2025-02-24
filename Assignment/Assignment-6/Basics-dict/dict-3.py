#3. Checking Key Existence
#Write a function check_key(d, key) that takes a dictionary d and a key key, and
#returns True if the key exists in the dictionary, otherwise False.

def check_key(d, key):
    if key in d:
        return True
    else: False
    
d = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(check_key(d,"model"))