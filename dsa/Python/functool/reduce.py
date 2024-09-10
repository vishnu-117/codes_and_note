from functools import reduce

# result = reduce(function, iterable)

def multiply(x, y):
    return x * y

result = reduce(multiply, [1,2,3,4])
print(result)

#using Lambda

result = reduce(lambda x, y: x * y, [1,2,3,4])
print(result)

#provide some initial value

result = reduce(lambda x, y: x * y, [1,2,3], 2) # 2 * 1 * 2 * 3
print(result)

# Example: Concatenating Strings
strings = ["Hello", " ", "World", "!"]
concatenated = reduce(lambda x,y: x + y, strings)
print(concatenated)

"""
The reduce(fun,seq) function is used to apply a particular function passed in
its argument to all of the list elements mentioned in the sequence passed along.
This function is defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
"""