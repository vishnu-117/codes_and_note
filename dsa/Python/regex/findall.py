import re
"""
3. re.findall(pattern, string)
Finds all occurrences of the pattern in the string and returns them as a list.
"""
pattern = r'\d+'
string = 'abc 123 def 456'

findall = re.findall(pattern, string)
print(findall)  # Output: ['123', '456']
