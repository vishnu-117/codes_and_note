import re

"""
2. re.search(pattern, string)
Searches for the first occurrence of the pattern anywhere in the string.
"""

pattern = r'\d+'
string = 'abc 123 def 456'

search = re.search(pattern, string)
if search:
    print(search.group())  # Output: "123"
else:
    print("No match")
