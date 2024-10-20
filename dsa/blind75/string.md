Here are Python solutions for the string-related problems:

---

### 1. **Longest Substring Without Repeating Characters**

Given a string, find the length of the longest substring without repeating characters.

#### Solution

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
```

#### Input/Output

**Input:**  
`"abcabcbb"`

**Output:**  
`3` (The answer is "abc", with a length of 3.)

---

### 2. **Longest Repeating Character Replacement**

Given a string `s` and an integer `k`, return the length of the longest substring containing the same letter you can get after performing at most `k` character replacements.

#### Solution

```python
def character_replacement(s, k):
    count = {}
    max_count = 0
    left = 0
    max_len = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])

        if right - left + 1 - max_count > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

#### Input/Output

**Input:**  
`s = "AABABBA", k = 1`

**Output:**  
`4` (Replace one "A" with "B" to get "BBBB".)

---

### 3. **Minimum Window Substring**

Given two strings `s` and `t`, return the minimum window in `s` which contains all the characters in `t`.

#### Solution

```python
from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    
    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while l <= r and formed == required:
            char = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            l += 1    
        r += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
```

#### Input/Output

**Input:**  
`s = "ADOBECODEBANC", t = "ABC"`

**Output:**  
`"BANC"` (Shortest substring containing all characters from `t`.)

---

### 4. **Valid Anagram**

Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.

#### Solution

```python
def is_anagram(s, t):
    return sorted(s) == sorted(t)
```

#### Input/Output

**Input:**  
`s = "anagram", t = "nagaram"`

**Output:**  
`True`

---

### 5. **Group Anagrams**

Given an array of strings, group anagrams together.

#### Solution

```python
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())
```

#### Input/Output

**Input:**  
`["eat", "tea", "tan", "ate", "nat", "bat"]`

**Output:**  
`[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

---

### 6. **Valid Parentheses**

Given a string `s` containing just the characters `('`, `')'`, `'{', `'}', `[` and `]`, determine if the input string is valid.

#### Solution

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack
```

#### Input/Output

**Input:**  
`"()[]{}"`

**Output:**  
`True`

---

### 7. **Valid Palindrome**

Given a string `s`, return `true` if the string is a palindrome when considering only alphanumeric characters and ignoring cases.

#### Solution

```python
def is_palindrome(s):
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    return filtered_chars == filtered_chars[::-1]
```

#### Input/Output

**Input:**  
`s = "A man, a plan, a canal: Panama"`

**Output:**  
`True`

---

### 8. **Longest Palindromic Substring**

Given a string `s`, return the longest palindromic substring in `s`.

#### Solution

```python
def longest_palindrome(s):
    if not s:
        return ""
    
    start, end = 0, 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
```

#### Input/Output

**Input:**  
`s = "babad"`

**Output:**  
`"bab"`

---

### 9. **Palindromic Substrings**

Given a string `s`, return the number of palindromic substrings in it.

#### Solution

```python
def count_substrings(s):
    count = 0

    for i in range(len(s)):
        count += expand_from_center(s, i, i)
        count += expand_from_center(s, i, i + 1)

    return count

def expand_from_center(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count
```

#### Input/Output

**Input:**  
`s = "aaa"`

**Output:**  
`6` (There are 6 palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".)

---

Let's continue solving the remaining string problems:

---

### 10. **Encode and Decode Strings (Leetcode Premium)**

You need to design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network, and you need to decode it back to the original list of strings.

The encoded string is a concatenation of each string with its length followed by a delimiter character. Let's use the delimiter `"#"` to separate each string's length and content.

#### Solution

```python
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded_list.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return decoded_list
```

#### Input/Output

**Input:**

```python
codec = Codec()
encoded = codec.encode(["hello", "world"])
decoded = codec.decode(encoded)
```

**Output:**

```python
Encoded: "5#hello5#world"
Decoded: ["hello", "world"]
```

---

### 11. **Valid Palindrome II**

Given a string `s`, return `true` if the string can be a palindrome after deleting at most one character from it.

#### Solution

```python
def valid_palindrome(s):
    def is_palindrome_range(i, j):
        return all(s[k] == s[j - k + i] for k in range(i, j))

    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            j = len(s) - 1 - i
            return is_palindrome_range(i + 1, j) or is_palindrome_range(i, j - 1)
    return True
```

#### Input/Output

**Input:**  
`s = "abca"`

**Output:**  
`True` (You can delete the character "c" to make it a palindrome: "aba".)

---

### 12. **Longest Palindromic Subsequence**

Given a string `s`, find the longest palindromic subsequence's length in `s`.

#### Solution

```python
def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
```

#### Input/Output

**Input:**  
`s = "bbbab"`

**Output:**  
`4` (The longest palindromic subsequence is "bbbb".)

---

### 13. **Valid Palindrome III**

You are given a string `s` and an integer `k`. Return `true` if `s` can be transformed into a palindrome by deleting at most `k` characters.

#### Solution

```python
def valid_palindrome_k(s, k):
    def longest_palindromic_subsequence(s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

    lps = longest_palindromic_subsequence(s)
    return len(s) - lps <= k
```

#### Input/Output

**Input:**  
`s = "abcdeca", k = 2`

**Output:**  
`True` (You can delete "b" and "e" to make it a palindrome "acdca".)

---

### 14. **Longest Subsequence Without Repeating Characters**

Given a string `s`, find the length of the longest subsequence without repeating characters.

#### Solution

```python
def length_of_longest_subsequence(s):
    last_index = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in last_index:
            start = max(start, last_index[char] + 1)
        last_index[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length
```

#### Input/Output

**Input:**  
`s = "abcabcbb"`

**Output:**  
`3` (The answer is "abc", with the length of 3.)

---

With this, we've solved a set of string-related problems using Python. Each problem has a unique solution and comes with examples to clarify the input-output format. Let me know if you need further explanations or additional problems to be solved!