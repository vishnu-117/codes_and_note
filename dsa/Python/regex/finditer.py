import re
"""
4. re.finditer(pattern, string)
Finds all occurrences of the pattern and returns an iterator of match objects.
"""
pattern = r'\d+'
string = 'abc 123 def 456'

for match in re.finditer(pattern, string):
    print(match.group())  # Output: "123" then "456"
