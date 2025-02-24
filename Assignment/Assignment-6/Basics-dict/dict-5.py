#5. Dictionary Length
#Write a function dict_length(d) that returns the number of key-value pairs in a
#given dictionary.

def dict_length(d):
    return len(d)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict_length(thisdict))