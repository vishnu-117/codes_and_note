import re
"""
1. re.match(pattern, string)
Checks for a match only at the beginning of the string.
"""
pattern = r'\d+'   # Matches one or more digits
string = '1234abc1234'

match = re.match(pattern, string)
if match:
    print(match.group())
else:
    print("No match")