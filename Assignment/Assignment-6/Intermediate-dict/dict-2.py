#7. Removing an Item from a Dictionary
#Given the dictionary:
#country_capitals = {
    # USA: Washington,
    # France: Paris,
    # India: New Delhi
    # }
    
def remove_item_dict(d, key):
    del d[key]
    return d
    
country_capitals = {
    "USA": "Washington",
    "France": "Paris",
    "India": "New Delhi"
}

print("Updated dictionary: ",remove_item_dict(country_capitals,"France"))