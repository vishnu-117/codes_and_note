import re
"""
6. re.split(pattern, string, maxsplit=0)
Splits the string by occurrences of the pattern. The maxsplit argument specifies the maximum number of splits.
"""
pattern = r'\d+'
string = 'abc 123 def 456'

split = re.split(pattern, string)
print(split)  # Output: ['abc ', ' def ', '']
