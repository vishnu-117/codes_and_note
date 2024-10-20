import re

text = "This is a test string!"

words = re.findall(r'[\S]+', text)

print(words)