# Dictionary = set of {key: value} pairs that are Changeable, No duplicates, Iterable
# Mapping of countries and their capitals

capitals = {"USA": "Washington D.C.",
            "Russia": "Moscow",
            "India": "New Delhi",
            "France": "Paris",
            "China": "Beijing"
            }

#print(help(capitals))
# Assigning variables for methods of values, keys, and items
value = capitals.values()
key = capitals.keys()
items = capitals.items()

# Iterating through the list of key, value pairs to print the items in a dictionary
for key,value in capitals.items():
    print(f"{key}: {value}")
