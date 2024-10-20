import re
"""
5. re.sub(pattern, repl, string)
Replaces occurrences of the pattern with a replacement string.
"""
pattern = r'\d+'
string = 'abc 123 def 456'
replacement = 'NUMBER'

result = re.sub(pattern, replacement, string)
print(result)  # Output: "abc NUMBER def NUMBER"
