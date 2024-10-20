Here are Python solutions for the given problems, focusing on Data Structures and Algorithms (DSA) and avoiding unnecessary built-in functions.

---

### 1. **Sum of Two Integers**

Calculate the sum of two integers without using the `+` or `-` operators.

#### Approach: Use bit manipulation. We simulate the addition process using XOR for sum and AND for the carry.

```python
def get_sum(a, b):
    MAX = 0x7FFFFFFF  # Maximum positive integer for 32-bit integer
    mask = 0xFFFFFFFF # Mask to get last 32 bits
    
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask  # XOR for sum, AND + shift for carry
    
    return a if a <= MAX else ~(a ^ mask)
```

---

### 2. **Number of 1 Bits**

Return the number of `1` bits (Hamming weight) in the binary representation of a number.

#### Approach: Use bit manipulation to count the number of set bits.

```python
def hamming_weight(n):
    count = 0
    while n:
        count += n & 1  # Check the last bit
        n >>= 1         # Right shift to check the next bit
    return count
```

---

### 3. **Counting Bits**

Given a number `n`, return an array of size `n+1` where `i`th element is the number of `1` bits in the binary representation of `i`.

#### Approach: Use dynamic programming. Use the result of previous numbers to build the current result.

```python
def count_bits(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)  # Use the result of i // 2 and add 1 if i is odd
    
    return dp
```

---

### 4. **Missing Number**

Given an array containing `n` distinct numbers taken from `0, 1, 2, ..., n`, find the one number that is missing.

#### Approach 1: Use the formula for the sum of the first `n` numbers. Subtract the actual sum of the array from the expected sum.

```python
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

#### Approach 2: XOR the indices and elements to cancel out everything except the missing number.

```python
def missing_number(nums):
    missing = len(nums)
    
    for i in range(len(nums)):
        missing ^= i ^ nums[i]
    
    return missing
```

---

### 5. **Reverse Bits**

Reverse the bits of a given 32-bit unsigned integer.

#### Approach: Bit by bit manipulation. Take each bit from the input and place it in the reverse position.

```python
def reverse_bits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)  # Shift result left and add the last bit of n
        n >>= 1  # Shift n right to process the next bit
    return result
```

---

These solutions employ bit manipulation, dynamic programming, and efficient mathematical approaches, avoiding unnecessary built-in Python functions.