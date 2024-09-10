import re
"""
8. re.escape(string)
Escapes all special characters in the string, so they can be used as literals in a regex pattern.
"""
special_string = 'hello. (world)?'
escaped_string = re.escape(special_string)
print(escaped_string)  # Output: 'hello\\. \\(world\\\\)\\?'
