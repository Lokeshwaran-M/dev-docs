
# Array



Create an empty list:
```python
my_list = []
```
Create a list with initial values:

```python
my_list = [1, 2, 3, 4, 5]
```
Access an element by index:

```python
element = my_list[index]
```
Modify an element by index:

```python
my_list[index] = new_value
```
Append an element to the end of the list:

```python
my_list.append(element)
```
Insert an element at a specific index:

```python
my_list.insert(index, element)
```
Remove an element by value:

```python
my_list.remove(element)
```
Remove an element by index:

```python
del my_list[index]
```
Check if an element exists in the list:

```python
element in my_list
```
Get the length of the list:

```python
length = len(my_list)
```
Sort the list in ascending order:

```python
my_list.sort()
```
Sort the list in descending order:

```python
my_list.sort(reverse=True)
```
Reverse the order of the list:

```python
my_list.reverse()
```
Concatenate two lists:

```python
combined_list = my_list1 + my_list2
```
Copy a list:

```python
new_list = my_list.copy()
```
Clear all elements from the list:

```python
my_list.clear()
```

Get the index of the first occurrence of an element:

```python
index = my_list.index(element)
```
Count the number of occurrences of an element in the list:

```python
count = my_list.count(element)
```
Extend the list by appending elements from another list:

```python
my_list.extend(another_list)
```
Slice the list to extract a subset of elements:

```python
subset = my_list[start:end]
```
Iterate over the elements of the list using a loop:

```python
for element in my_list:
    # Do something with element
```
Check if the list is empty:

```python
if not my_list:
    # List is empty
```
Check the minimum element in the list:

```python
minimum = min(my_list)
```
Check the maximum element in the list:

```python
maximum = max(my_list)
```
Check the sum of all elements in the list:

```python
total = sum(my_list)
```
Check if all elements in the list satisfy a condition:

```python
all_true = all(condition for element in my_list)
```
Check if any element in the list satisfies a condition:

```python
any_true = any(condition for element in my_list)
```
Remove and return the last element from the list:

```python
last_element = my_list.pop()
```
Remove and return the element at a specific index:

```python
removed_element = my_list.pop(index)
```
convert a list to a string:

```python
list_string = ', '.join(str(element) for element in my_list)
```

Check if any element in the list does not satisfy a condition:

```python
any_false = any(not condition for element in my_list)
```
Find the first element that satisfies a condition:

```python
first_element = next(element for element in my_list if condition)
```
Find the index of the first element that satisfies a condition:

```python
index = next(index for index, element in enumerate(my_list) if condition)
```
Remove all occurrences of an element from the list:

```python
my_list = [element for element in my_list if element != target_element]
```
Create a new list by applying a function to each element:

```python
new_list = [function(element) for element in my_list]
```
Filter elements in the list based on a condition:

```python
filtered_list = [element for element in my_list if condition]
```
Find the unique elements in the list:

```python
unique_list = list(set(my_list))
```
Iterate over the list in reverse order:

```python
for element in reversed(my_list):

    # Do something with element
```
Check if the list is sorted in ascending order:

```python
is_sorted = all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))
```
Concatenate multiple lists into a single list:

```python
concatenated_list = [element for sublist in list_of_lists for element in sublist]
```