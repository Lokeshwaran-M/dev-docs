# Create an array
my_array = [1, 2, 3, 4, 5]

# Accessing elements in the array
print(my_array[0])  # Access element at index 0
print(my_array[-1])  # Access last element

# Updating elements in the array
my_array[2] = 10  # Update element at index 2

# Length of the array
length = len(my_array)
print(length)

# Adding elements to the array
my_array.append(6)  # Add an element to the end of the array
my_array.insert(2, 7)  # Insert an element at index 2

# Removing elements from the array
my_array.remove(4)  # Remove the first occurrence of 4
my_array.pop()  # Remove and return the last element
del my_array[1]  # Remove element at index 1

# Slicing the array
sliced_array = my_array[1:4]  # Get a portion of the array from index 1 to 3

# Sorting the array
my_array.sort()  # Sort the array in ascending order
my_array.reverse()  # Reverse the order of elements

# Searching for an element in the array
index = my_array.index(3)  # Get the index of the first occurrence of 3
is_present = 5 in my_array  # Check if 5 is present in the array

# Counting occurrences of an element
count = my_array.count(2)  # Count the number of occurrences of 2

# Concatenating arrays
concatenated_array = my_array + [8, 9, 10]

# Copying an array
copy_array = my_array.copy()

# Clearing an array
my_array.clear()

# Iterate over the elements of the array
for element in my_array:
    print(element)


# Checking if an array is empty
is_empty = len(my_array) == 0

# Extending an array with another array
my_array.extend([11, 12, 13])

# Reversing the order of elements in the array
reversed_array = list(reversed(my_array))

# Finding the maximum and minimum values in the array
max_value = max(my_array)
min_value = min(my_array)

# Summing the elements in the array
sum_of_elements = sum(my_array)

# Finding the average of elements in the array
average = sum(my_array) / len(my_array)

# Checking if all elements satisfy a condition
all_positive = all(x > 0 for x in my_array)

# Checking if any element satisfies a condition
any_even = any(x % 2 == 0 for x in my_array)

# Mapping a function to each element of the array
mapped_array = list(map(lambda x: x * 2, my_array))

# Filtering elements based on a condition
filtered_array = list(filter(lambda x: x % 2 == 0, my_array))

# Enumerating elements with their indices
for index, element in enumerate(my_array):
    print(f"Index: {index}, Element: {element}")

# Concatenating arrays using the + operator
concatenated_array = my_array + [14, 15, 16]

# Repeating an array multiple times
repeated_array = my_array * 3

# Checking if two arrays are equal
is_equal = my_array == [1, 2, 3, 4, 5]

# Converting an array to a string
array_string = str(my_array)

# Sorting an array in a customized order
my_array.sort(key=lambda x: x % 3)  # Sort based on remainder when divided by 3



# Checking if an element exists in the array using the 'in' operator
is_present = 7 in my_array

# Finding the index of the last occurrence of an element
last_index = my_array.index(5)

# Counting the number of occurrences of an element
count = my_array.count(3)

# Removing all occurrences of an element from the array
my_array = [x for x in my_array if x != 2]

# Extracting unique elements from the array
unique_array = list(set(my_array))

# Copying an array using the slicing technique
copied_array = my_array[:]

# Replacing specific elements in the array
my_array[1:4] = [8, 9, 10]

# Checking if two arrays have any common elements
has_common_elements = any(x in my_array for x in other_array)

# Resizing the array by changing its length
my_array = my_array[:5]  # Truncate the array to a length of 5

# Iterating over the array using list comprehension
squared_array = [x**2 for x in my_array]

# Applying a function to each element of the array using list comprehension
transformed_array = [my_function(x) for x in my_array]

# Flattening a nested array
nested_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_array = [item for sublist in nested_array for item in sublist]

# Sorting the array based on a specific criterion
my_array.sort(key=lambda x: abs(x - 5))  # Sort based on the absolute difference from 5
