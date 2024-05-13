# in python, the word iterate simply means to loop over a data-structure with a for-loop
# to retrieve all the elements in the data-structure

# the following dict has keys that are strings and values that are integers
ages = {"Matt": 23, "John": 40, "Anna": 33, "Patti": 40}

print()
print("printing all keys in the dict")
# the default way to iterate over a dict is to just retrieve each of the keys.
for name in ages:
  print(f"the next persons name is {name}")
print()
print("printing all values in the dict")
# if you want to retrieve the values, you need to use the dict method `values()`
for age in ages:
  print(f"the next age is {age}")
print()
print("printing all keys and values in the dict")
# if you want both the keys and the values, you need to use the `items()` method.
for name, age in ages.items():
  print(f"{name} is {age} years old")
