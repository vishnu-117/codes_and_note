Here’s a breakdown of how to solve the listed problems first using **backtracking/recursion** and then optimizing them using **dynamic programming (DP)**.

---

### 1. **Climbing Stairs**

You are climbing a staircase. You can either take 1 step or 2 steps. Find how many distinct ways you can reach the top.

#### Backtracking (Recursion)

```python
def climb_stairs(n):
    if n <= 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)
```

#### Dynamic Programming

```python
def climb_stairs_dp(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

---

### 2. **Coin Change**

Given coins of different denominations and a total amount, find the minimum number of coins needed to make up that amount.

#### Backtracking (Recursion)

```python
def coin_change(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
        res = coin_change(coins, amount - coin)
        min_coins = min(min_coins, res + 1)
    
    return min_coins
```

#### Dynamic Programming

```python
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

---

### 3. **Longest Increasing Subsequence**

Find the length of the longest increasing subsequence in an array.

#### Backtracking (Recursion)

```python
def lis_recursive(nums, i, prev):
    if i == len(nums):
        return 0
    
    take = 0
    if nums[i] > prev:
        take = 1 + lis_recursive(nums, i + 1, nums[i])
    skip = lis_recursive(nums, i + 1, prev)
    
    return max(take, skip)
```

#### Dynamic Programming

```python
def lis_dp(nums):
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

---

### 4. **Longest Common Subsequence**

Find the longest common subsequence between two strings.

#### Backtracking (Recursion)

```python
def lcs_recursive(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + lcs_recursive(s1, s2, i + 1, j + 1)
    else:
        return max(lcs_recursive(s1, s2, i + 1, j), lcs_recursive(s1, s2, i, j + 1))
```

#### Dynamic Programming

```python
def lcs_dp(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]
```

---

### 5. **Word Break Problem**

Given a string and a dictionary of words, determine if the string can be segmented into a space-separated sequence of dictionary words.

#### Backtracking (Recursion)

```python
def word_break(s, word_dict):
    if not s:
        return True
    
    for i in range(1, len(s) + 1):
        if s[:i] in word_dict and word_break(s[i:], word_dict):
            return True
    return False
```

#### Dynamic Programming

```python
def word_break_dp(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[-1]
```

---

### 6. **Combination Sum**

Given an array of distinct integers and a target, return all unique combinations of the numbers that sum to the target.

#### Backtracking (Recursion)

```python
def combination_sum(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(list(current))
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()
    
    result = []
    backtrack(0, [], target)
    return result
```

#### Dynamic Programming

This problem does not have a direct DP solution like the others. It’s inherently backtracking-based.

---

### 7. **House Robber**

You cannot rob two adjacent houses. Determine the maximum amount of money you can rob.

#### Backtracking (Recursion)

```python
def rob_recursive(nums, i):
    if i >= len(nums):
        return 0
    return max(rob_recursive(nums, i + 2) + nums[i], rob_recursive(nums, i + 1))
```

#### Dynamic Programming

```python
def rob_dp(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]
```

---

### 8. **House Robber II**

Same as above, but houses are arranged in a circle.

#### Backtracking (Recursion)

```python
def rob_recursive(nums, i):
    if i >= len(nums):
        return 0
    return max(rob_recursive(nums, i + 2) + nums[i], rob_recursive(nums, i + 1))
```

#### Dynamic Programming

```python
def rob_dp(nums):
    if len(nums) == 1:
        return nums[0]
    
    def rob_line(nums):
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
    
    return max(rob_line(nums[1:]), rob_line(nums[:-1]))
```

---

### 9. **Decode Ways**

Given a string of digits, return how many ways it can be decoded (mapping `1` to `A`, `2` to `B`, etc.).

#### Backtracking (Recursion)

```python
def num_decodings_recursive(s, index):
    if index == len(s):
        return 1
    if s[index] == '0':
        return 0
    
    count = num_decodings_recursive(s, index + 1)
    
    if index < len(s) - 1 and (s[index] == '1' or (s[index] == '2' and s[index + 1] in '0123456')):
        count += num_decodings_recursive(s, index + 2)
    
    return count
```

#### Dynamic Programming

```python
def num_decodings_dp(s):
    if not s or s[0] == '0':
        return 0
    dp = [0] * (len(s) + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if s[i - 2:i] >= '10' and s[i - 2:i] <= '26':
            dp[i] += dp[i - 2]
    
    return dp[-1]
```

---

### 10. **Unique Paths**

A robot can move right or down in an `m x n` grid. The goal is to find how many unique paths exist from the top-left corner to the bottom-right corner.

#### Backtracking (Recursion)

In the recursive approach, at each position, you can either move right or down, and you explore all possible paths.

```python
def unique_paths_recursive(m, n):
    # Base case: if the robot reaches the bottom or right edge, there is only one path (straight down or right).
    if m == 1 or n == 1:
        return 1
    # Explore both moving right and down.
    return unique_paths_recursive(m - 1, n) + unique_paths_recursive(m, n - 1)
```

#### Dynamic Programming

To optimize, we use dynamic programming by building a 2D DP table where `dp[i][j]` represents the number of unique paths to reach position `(i, j)`.

```python
def unique_paths_dp(m, n):
    # Initialize a 2D array where each cell is set to 1 (since the first row and first column have only 1 path).
    dp = [[1] * n for _ in range(m)]
    
    # Start filling from cell (1, 1), because the first row and first column are all 1.
    for i in range(1, m):
        for j in range(1, n):
            # The number of paths to a cell is the sum of paths from the cell above and the cell to the left.
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # The bottom-right corner contains the total number of unique paths.
    return dp[m - 1][n - 1]
```

---

### 11. **Jump Game**

Given an array where each element represents the maximum number of steps you can take from that position, determine if you can reach the last index.

#### Backtracking (Recursion)

In the recursive approach, we attempt to jump from the current position to any reachable position and recursively check if we can reach the end.

```python
def can_jump_recursive(nums, position=0):
    # Base case: If the current position is the last index, return True.
    if position >= len(nums) - 1:
        return True
    
    # The furthest we can jump from the current position.
    furthest_jump = min(position + nums[position], len(nums) - 1)
    
    # Try every jump length from the current position.
    for next_position in range(position + 1, furthest_jump + 1):
        if can_jump_recursive(nums, next_position):
            return True
    
    return False
```

#### Dynamic Programming

To optimize, we can use a greedy approach or a DP approach. The greedy approach works in this case, as we just need to track the furthest point we can reach at each step.

```python
def can_jump_greedy(nums):
    furthest_reach = 0
    
    for i in range(len(nums)):
        if i > furthest_reach:  # If the current index is beyond the furthest we can reach, return False.
            return False
        # Update the furthest point we can reach.
        furthest_reach = max(furthest_reach, i + nums[i])
    
    return True
```

---

These solutions first use **backtracking/recursion** to explore the problem and then are optimized using **dynamic programming** or **greedy** methods for better time complexity. Let me know if you'd like detailed explanations on specific optimizations or any other problems!

