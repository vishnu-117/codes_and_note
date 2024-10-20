"""
1. str.capitalize()

s = "hello world"
print(s.capitalize())  # Output: "Hello world"

2. str.casefold()

3. str.center(width, fillchar)

s = "python"
print(s.center(10, '*'))  # Output: "**python**"

4. str.count(substring, start=0, end=len(string))

s = "banana"
print(s.count('a'))  # Output: 3
print(s.count('a', 2, 5))  # Output: 1


5. str.encode(encoding='utf-8', errors='strict')

s = "hello"
print(s.encode())  # Output: b'hello'


6. str.endswith(suffix, start=0, end=len(string))

s = "example.txt"
print(s.endswith('.txt'))  # Output: True
print(s.endswith('.doc'))  # Output: False

7. str.expandtabs(tabsize=8)

s = "hello\tworld"
print(s.expandtabs())  # Output: "hello   world"
print(s.expandtabs(4))  # Output: "hello  world"

8. str.find(substring, start=0, end=len(string))

s = "hello world"
print(s.find('world'))  # Output: 6
print(s.find('Python'))  # Output: -1

9. str.format(*args, **kwargs)

template = "Hello, {}. Welcome to {}!"
print(template.format("Alice", "Wonderland"))  # Output: "Hello, Alice. Welcome to Wonderland!"

10. str.format_map(mapping)

template = "Hello, {name}. Welcome to {place}!"
data = {'name': 'Bob', 'place': 'Narnia'}
print(template.format_map(data))  # Output: "Hello, Bob. Welcome to Narnia!"

11. str.index(substring, start=0, end=len(string))

s = "hello world"
print(s.index('world'))  # Output: 6

12. str.isalnum()

s = "hello123"
print(s.isalnum())  # Output: True
print("hello@123".isalnum())  # Output: False

13. str.isalpha()

s = "hello"
print(s.isalpha())  # Output: True
print("hello123".isalpha())  # Output: False


14. str.isascii()

s = "hello"
print(s.isascii())  # Output: True
print("こんにちは".isascii())  # Output: False

15. str.isdigit()

s = "12345"
print(s.isdigit())  # Output: True
print("123a45".isdigit())  # Output: False

16. str.islower()

s = "hello"
print(s.islower())  # Output: True
print("Hello".islower())  # Output: False


17. str.isnumeric()

s = "12345"
print(s.isnumeric())  # Output: True
print("12.34".isnumeric())  # Output: False


18. str.isspace()

s = "   "
print(s.isspace())  # Output: True
print("hello".isspace())  # Output: False

19. str.istitle()

s = "Hello World"
print(s.istitle())  # Output: True
print("Hello world".istitle())  # Output: False


20. str.isupper()


s = "HELLO"
print(s.isupper())  # Output: True
print("Hello".isupper())  # Output: False


21. str.join(iterable)

words = ["hello", "world"]
print(", ".join(words))  # Output: "hello, world"


22. str.ljust(width, fillchar)

s = "hello"
print(s.ljust(10, '*'))  # Output: "hello*****"


23. str.lstrip(chars)

s = "   hello   "
print(s.lstrip())  # Output: "hello   "
print("xxhello".lstrip('x'))  # Output: "hello"


24. str.partition(sep)

s = "hello world"
print(s.partition(' '))  # Output: ('hello', ' ', 'world')


25. str.replace(old, new, count)

s = "hello world"
print(s.replace('world', 'Python'))  # Output: "hello Python"
print(s.replace('o', 'O', 1))  # Output: "hellO world"


26. str.rfind(substring, start=0, end=len(string))
s = "hello world, hello universe"
print(s.rfind('hello'))  # Output: 13
print(s.rfind('Python'))  # Output: -1


27. str.rindex(substring, start=0, end=len(string))

s = "hello world, hello universe"
print(s.rindex('hello'))  # Output: 13


28. str.rjust(width, fillchar)

s = "hello"
print(s.rjust(10, '*'))  # Output: "*****hello"


29. str.rsplit(sep, maxsplit)
s = "one,two,three,four"
print(s.rsplit(',', 2))  # Output: ['one,two', 'three', 'four']

30. str.rstrip(chars)
s = "   hello   "
print(s.rstrip())  # Output: "   hello"
print("hello***".rstrip('*'))  # Output: "hello"

31. str.split(sep, maxsplit)
s = "one two three"
print(s.split())  # Output: ['one', 'two', 'three']
print(s.split(' ', 1))  # Output: ['one', 'two three']


32. str.splitlines(keepends=False)
s = "line1\nline2\nline


"""