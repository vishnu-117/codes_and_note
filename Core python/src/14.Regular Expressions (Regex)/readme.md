### Regular Expressions in Python

Python provides a module named `re` to work with **regular expressions (regex)**, which is a powerful tool for matching patterns in text. Regular expressions allow for pattern-based search, extraction, and manipulation of strings.

---

### **Basic Concepts**

- **Regular Expression (Regex)**: A sequence of characters that defines a search pattern.
- **Pattern Matching**: Regex patterns can match sequences of characters in a string (e.g., digits, letters, special characters).
  
---

### **Python `re` Module Functions**

1. **`re.match()`**:
   - Tries to match a pattern **at the beginning** of the string.
   - **When to use**: To check if the string starts with a specific pattern.
   - **Example**:
     ```python
     import re
     pattern = r'\d+'  # Matches one or more digits
     string = '123abc'
     match = re.match(pattern, string)
     if match:
         print(match.group())  # Output: 123
     ```

2. **`re.search()`**:
   - Searches the entire string for a pattern and returns the **first match**.
   - **When to use**: To search for the first occurrence of a pattern anywhere in the string.
   - **Example**:
     ```python
     match = re.search(r'\d+', 'abc123def')
     if match:
         print(match.group())  # Output: 123
     ```

3. **`re.findall()`**:
   - Returns a **list of all non-overlapping matches** of the pattern in the string.
   - **When to use**: To find all occurrences of a pattern in the string.
   - **Example**:
     ```python
     matches = re.findall(r'\d+', 'abc123def456ghi789')
     print(matches)  # Output: ['123', '456', '789']
     ```

4. **`re.finditer()`**:
   - Returns an **iterator** yielding match objects for all non-overlapping matches of the pattern.
   - **When to use**: When you want to iterate over matches and extract details like position and value.
   - **Example**:
     ```python
     matches = re.finditer(r'\d+', 'abc123def456ghi789')
     for match in matches:
         print(match.group())  # Outputs: 123, 456, 789
     ```

5. **`re.sub()`**:
   - Replaces occurrences of the pattern with a specified replacement string.
   - **When to use**: To perform substitutions or text replacement.
   - **Example**:
     ```python
     result = re.sub(r'\d+', 'X', 'abc123def456')
     print(result)  # Output: abcXdefX
     ```

6. **`re.split()`**:
   - Splits the string by occurrences of the pattern.
   - **When to use**: To split a string based on a specific pattern.
   - **Example**:
     ```python
     result = re.split(r'\d+', 'abc123def456ghi789')
     print(result)  # Output: ['abc', 'def', 'ghi', '']
     ```

---

### **Common Regex Patterns**

- **`\d`**: Matches any digit (0-9).
- **`\D`**: Matches any non-digit character.
- **`\w`**: Matches any alphanumeric character (letters, digits, and underscore).
- **`\W`**: Matches any non-alphanumeric character.
- **`\s`**: Matches any whitespace character (space, tab, newline).
- **`\S`**: Matches any non-whitespace character.
- **`.`**: Matches any character except newline.
- **`^`**: Matches the start of a string.
- **`$`**: Matches the end of a string.
- **`*`**: Matches 0 or more repetitions of the preceding pattern.
- **`+`**: Matches 1 or more repetitions of the preceding pattern.
- **`?`**: Matches 0 or 1 repetition of the preceding pattern.
- **`{n}`**: Matches exactly `n` occurrences of the preceding pattern.
- **`{n,}`**: Matches `n` or more occurrences of the preceding pattern.
- **`{n,m}`**: Matches between `n` and `m` occurrences.
- **`[...]`**: Matches any character inside the brackets (e.g., `[abc]` matches 'a', 'b', or 'c').
- **`|`**: Acts like a logical OR (e.g., `a|b` matches 'a' or 'b').

---

### **Advanced Features**

1. **Groups and Capturing**:
   - Parentheses `()` are used to define groups, which capture parts of the string.
   - **Example**:
     ```python
     match = re.search(r'(\d{3})-(\d{2})-(\d{4})', 'My number is 123-45-6789')
     if match:
         print(match.group(1))  # Output: 123
         print(match.group(2))  # Output: 45
         print(match.group(3))  # Output: 6789
     ```

2. **Non-Capturing Groups**:
   - Use `(?:...)` for non-capturing groups, meaning they won’t be stored as separate groups.
   - **Example**:
     ```python
     match = re.search(r'(?:abc)(\d+)', 'abc123')
     print(match.group(1))  # Output: 123 (does not capture 'abc')
     ```

3. **Lookahead and Lookbehind Assertions**:
   - **Lookahead**: Ensures that a pattern is followed by another pattern, without including it in the match.
     - **Example**:
       ```python
       result = re.search(r'\d+(?= dollars)', 'The price is 100 dollars')
       print(result.group())  # Output: 100
       ```
   - **Lookbehind**: Ensures that a pattern is preceded by another pattern.
     - **Example**:
       ```python
       result = re.search(r'(?<=\$)\d+', 'The price is $100')
       print(result.group())  # Output: 100
       ```

4. **Flags**:
   - Flags modify the behavior of regex matching.
   - **Common flags**:
     - `re.IGNORECASE` (`re.I`): Case-insensitive matching.
     - `re.MULTILINE` (`re.M`): `^` and `$` match the start/end of each line.
     - `re.DOTALL` (`re.S`): `.` matches newline characters as well.
   - **Example**:
     ```python
     match = re.search(r'hello', 'Hello World', re.IGNORECASE)
     print(match.group())  # Output: Hello
     ```

---

### **Example Use Cases**

1. **Email Validation**:
   ```python
   email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
   email = 'example@domain.com'
   if re.match(email_pattern, email):
       print("Valid email")
   ```

2. **Phone Number Matching**:
   ```python
   phone_pattern = r'\d{3}-\d{3}-\d{4}'
   phone = '123-456-7890'
   if re.match(phone_pattern, phone):
       print("Valid phone number")
   ```

3. **Extracting All Numbers from a String**:
   ```python
   text = "There are 3 apples, 7 oranges, and 15 bananas."
   numbers = re.findall(r'\d+', text)
   print(numbers)  # Output: ['3', '7', '15']
   ```

---

### **Summary**

- The `re` module provides functions like `match()`, `search()`, `findall()`, and `sub()` for working with regular expressions.
- Regex patterns can be used to perform tasks such as pattern matching, data extraction, and string substitution.
- Advanced features like groups, lookaheads, lookbehinds, and flags allow for more complex pattern matching.