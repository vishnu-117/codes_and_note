# map(function, iterable, ...)
"""
The map function in Python applies a given function to all items in an input
iterable (such as a list) and returns a map object (an iterator) of the results.
It is useful for transforming data in a concise and readable way.
"""
numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n

result = list(map(square, numbers))
print(result)

print('=============================================================')
strings = ["hello", "world", "python"]

# Use map with the str.upper method to convert strings to uppercase
uppercase_strings = list(map(str.upper, strings))

print(uppercase_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']
print('=============================================================')

list1 = [1, 2, 3]
list2 = [4, 5, 6]

def  add(x, y):
    return x + y

result = list(map(add, list1, list2))
print(result)

