"""
This program provides very basic examples of how to create and use dictionaries
"""


# create empty dictionary
genres = {}

# add key-value pairs to the dictionary
## dict_name[key] = value
## keys can be any type and so can values, in this case the keys and values are both strings
genres["Metallica"] = "metal"
genres["Snoop Dogg"] = "rap"
genres["Mozart"] = "Classical"

# retrieve value by providing key
## value_for_provided_key = dict_name[key]
metallica_genre = genres["Metallica"]
print(f'Metallica is a {metallica_genre} band')

# create a pre-filled dictionary
## dict_name = {key1: val1, key2: val2 ...}
ages = {"bill": 56, "mike": 23, "marry": 31}

name = "mike"
print(f'{name} is {ages[name]} years old')

# create a dict of dicts
"""
dict_name = {
    key: {
        inner_key1: inner_value1,
        inner_key2: inner_value2
    },
    key2: {
        inner_key1: inner_value1,
        inner_key2: inner_value2
    }
}
"""
menu = {
    "breakfast": {
    "eggs", 1.99,
    "pancakes", 2.89,
    "hash-browns", 3.99
    }, 
    "lunch": {
    "salad": 3.49,
    "sandwich": 7.99,
    "burger": 5.99
    }
}

print(menu["breakfast"])
