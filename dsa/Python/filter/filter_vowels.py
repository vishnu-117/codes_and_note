"""
The filter() method filters the given sequence with the help of a function 
that tests each element in the sequence to be true or not. 
"""

# filter(function, iterable)

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

def filter_vowels(data):
    vowels_list = ['a', 'e', 'i', 'o', 'u']

    if data in vowels_list:
        return True
    return False

vowels_result = list(filter(filter_vowels, sequence))
print(vowels_result)