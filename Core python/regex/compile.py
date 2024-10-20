import re
"""
7. re.compile(pattern, flags=0)
Compiles a pattern into a regex object, which can be used for matching, searching, and other operations. Flags modify the regex behavior.
"""
pattern = re.compile(r'\d+', re.IGNORECASE)
string = 'ABC 123 def'

match = pattern.search(string)
if match:
    print(match.group())  # Output: "123"
