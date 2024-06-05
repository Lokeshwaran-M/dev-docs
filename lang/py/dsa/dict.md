# Dictnory ( Hash Map)

```python

# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs to the dictionary
my_dict["apple"] = 10
my_dict["banana"] = 5
my_dict["orange"] = 7

# Accessing values using keys
print(my_dict["apple"])  # Output: 10

# Checking if a key exists in the dictionary
print("banana" in my_dict)  # Output: True
print("grape" in my_dict)  # Output: False

# Updating the value for a key
my_dict["apple"] = 15
print(my_dict["apple"])  # Output: 15

# Removing a key-value pair from the dictionary
del my_dict["orange"]
print(my_dict)  # Output: {'apple': 15, 'banana': 5}

# Getting the number of key-value pairs in the dictionary
print(len(my_dict))  # Output: 2

# Iterating over keys in the dictionary
for key in my_dict:
    print(key)  # Output: apple, banana

# Iterating over values in the dictionary
for value in my_dict.values():
    print(value)  # Output: 15, 5

# Iterating over key-value pairs in the dictionary
for key, value in my_dict.items():
    print(key, value)  # Output: apple 15, banana 5

```

```python

# Copying a dictionary
new_dict = my_dict.copy()
print(new_dict)  # Output: {'apple': 15, 'banana': 5}

# Clearing all key-value pairs from a dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Merging two dictionaries
dict1 = {"apple": 10, "banana": 5}
dict2 = {"orange": 7, "grape": 3}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'apple': 10, 'banana': 5, 'orange': 7, 'grape': 3}

# Getting a list of keys
keys = list(my_dict.keys())
print(keys)  # Output: []

# Getting a list of values
values = list(my_dict.values())
print(values)  # Output: []

# Getting a default value for a non-existing key
default_value = my_dict.get("apple", 0)
print(default_value)  # Output: 0

# Getting a default value for a non-existing key and adding it to the dictionary
default_value = my_dict.setdefault("apple", 0)
print(my_dict)  # Output: {'apple': 0}

# Removing and returning a key-value pair from the dictionary
removed_pair = my_dict.popitem()
print(removed_pair)  # Output: ('apple', 0)
print(my_dict)  # Output: {}

# Updating a dictionary with key-value pairs from another dictionary
dict1.update(dict2)
print(dict1)  # Output: {'apple': 10, 'banana': 5, 'orange': 7, 'grape': 3}

```

```python

# Removing a key-value pair and returning its value
value = my_dict.pop("apple")
print(value)  # Output: 10
print(my_dict)  # Output: {'banana': 5, 'orange': 7}

# Creating a dictionary with default values
from collections import defaultdict

default_dict = defaultdict(int)
default_dict["apple"] = 10
print(default_dict["banana"])  # Output: 0 (default value for int)

# Creating a dictionary from two lists
keys = ["apple", "banana", "orange"]
values = [10, 5, 7]

combined_dict = dict(zip(keys, values))
print(combined_dict)  # Output: {'apple': 10, 'banana': 5, 'orange': 7}

# Checking if all keys satisfy a condition
all_keys_satisfy = all(key > 0 for key in my_dict.keys())
print(all_keys_satisfy)  # Output: True

# Checking if any key satisfies a condition
any_key_satisfies = any(key == "apple" for key in my_dict.keys())
print(any_key_satisfies)  # Output: False

# Sorting a dictionary by keys
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)  # Output: {'banana': 5, 'orange': 7}

# Sorting a dictionary by values
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict)  # Output: {'banana': 5, 'orange': 7}

```

```python

# Getting a list of key-value pairs as tuples
items = list(my_dict.items())
print(items)  # Output: [('banana', 5), ('orange', 7)]

# Checking if a value exists in the dictionary
print(5 in my_dict.values())  # Output: True

# Getting a list of all keys or values
keys = my_dict.keys()
values = my_dict.values()
print(keys)  # Output: dict_keys(['banana', 'orange'])
print(values)  # Output: dict_values([5, 7])

# Updating a dictionary with key-value pairs from an iterable
my_dict.update([("apple", 10), ("grape", 3)])
print(my_dict)  # Output: {'banana': 5, 'orange': 7, 'apple': 10, 'grape': 3}

# Iterating over key-value pairs using a for loop
for key, value in my_dict.items():
    print(key, value)  # Output: banana 5, orange 7, apple 10, grape 3

# Creating a dictionary with a default value factory
from collections import defaultdict

default_dict = defaultdict(lambda: "N/A")
print(default_dict["unknown_key"])  # Output: N/A

# Converting dictionary keys or values to a set
key_set = set(my_dict.keys())
value_set = set(my_dict.values())
print(key_set)  # Output: {'banana', 'orange'}
print(value_set)  # Output: {5, 7}

# Getting a list of unique values from the dictionary
unique_values = list(set(my_dict.values()))
print(unique_values)  # Output: [5, 7]

```