Here's a collection of Python solutions for the given problems, avoiding built-in functions as much as possible and focusing on using Data Structures and Algorithms (DSA).

---

### 1. **Two Sum**

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

#### Approach: Using a Hash Map for fast lookups.

```python
def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i
```

---

### 2. **Best Time to Buy and Sell Stock**

Find the maximum profit you can achieve by buying and selling one stock.

#### Approach: Track the minimum price and compare each price with the minimum.

```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit
```

---

### 3. **Contains Duplicate**

Check if a list contains any duplicates.

#### Approach: Use a Set to track seen elements.

```python
def contains_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False
```

---

### 4. **Product of Array Except Self**

Return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

#### Approach: Two passes (left to right, then right to left).

```python
def product_except_self(nums):
    length = len(nums)
    left_products = [1] * length
    right_products = [1] * length
    output = [1] * length
    
    for i in range(1, length):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    for i in range(length - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    for i in range(length):
        output[i] = left_products[i] * right_products[i]
    
    return output
```

---

### 5. **Maximum Subarray**

Find the contiguous subarray with the largest sum.

#### Approach: Kadane's Algorithm.

```python
def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

---

### 6. **Maximum Product Subarray**

Find the contiguous subarray with the largest product.

#### Approach: Track the maximum and minimum products at each position.

```python
def max_product_subarray(nums):
    if not nums:
        return 0
    
    max_product = min_product = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result
```

---

### 7. **Find Minimum in Rotated Sorted Array**

Find the minimum element in a rotated sorted array.

#### Approach: Binary Search.

```python
def find_min(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]
```

---

### 8. **Search in Rotated Sorted Array**

Search for a target value in a rotated sorted array.

#### Approach: Binary Search with conditions.

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

---

### 9. **3Sum**

Find all unique triplets in the array which gives the sum of zero.

#### Approach: Sort and use two pointers.

```python
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result
```

---

### 10. **Container With Most Water**

Find two lines that together with the x-axis form a container which contains the most water.

#### Approach: Two pointers.

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        max_area = max(max_area, width * min(height[left], height[right]))
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
```

---

These solutions use core algorithms and data structures like hash maps, two pointers, dynamic programming, binary search, and others while avoiding unnecessary built-in functions.


















When solving array or list-based problems, several common patterns can be applied to simplify the problem-solving process. Here are some of the most prevalent patterns:

### 1. **Sliding Window**
This pattern is useful for problems involving subarrays or substrings. It helps in finding maximums, minimums, or other properties within a contiguous segment of the array.

**Example Problem:** Maximum Sum Subarray of Size K
```python
def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = sum(arr[:k])
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 2. **Two Pointers**
This approach uses two pointers to traverse the array, often from different ends. It's useful for problems that require checking pairs or partitioning.

**Example Problem:** Container With Most Water
```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

### 3. **Binary Search**
This pattern is commonly used when the array is sorted or when searching for a target value. It can also be applied to problems that can be transformed into a search problem.

**Example Problem:** Search in Rotated Sorted Array
```python
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[right]:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1
```

### 4. **Dynamic Programming (DP)**
This pattern is used for optimization problems where the solution can be built from previously solved subproblems. It often involves creating a table to store intermediate results.

**Example Problem:** Climbing Stairs
```python
def climb_stairs(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

### 5. **Backtracking**
This pattern is often used for combinatorial problems, where you explore all potential solutions and backtrack when you reach an invalid state.

**Example Problem:** Subsets
```python
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    
    backtrack(0, [])
    return result
```

### 6. **Prefix Sum**
This technique is used to preprocess sums of subarrays for efficient range queries. It is useful when calculating sums of segments frequently.

**Example Problem:** Subarray Sum Equals K
```python
def subarray_sum(nums, k):
    count = 0
    prefix_sum = {0: 1}
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return count
```

### 7. **Sorting and Hashing**
Some problems can be simplified by sorting the array or using hash tables for counting occurrences, finding duplicates, or checking for conditions.

**Example Problem:** Group Anagrams
```python
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())
```

### Conclusion
These patterns provide a structured approach to tackle various array or list problems efficiently. Familiarizing yourself with these can significantly enhance your problem-solving skills in coding interviews or competitive programming.