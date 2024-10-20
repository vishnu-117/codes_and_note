def has_subarray_with_sum_k(arr, k):
    """
    T.C: O(n), S.C: O(n)
    """
    prefix_sum = 0
    prefix_set = set()

    for num in arr:
        prefix_sum += num

        if prefix_sum == k:
            return True
        
        if prefix_sum - k in prefix_set:
            return True
        
        prefix_set.add(prefix_sum)
    
    return False

# Example usage
arr = [10, 15, -5, 15, -10, 5]
K = 20
result = has_subarray_with_sum_k(arr, K)
print(result)  

######################################
# count no of subarra with sum k

def count_subarrays_with_sum_k(arr, K):
    prefix_sum = 0
    prefix_map = {}
    count = 0

    for num in arr:
        prefix_sum += num

        if prefix_sum == K:
            count += 1

        if (prefix_sum - K) in prefix_map:
            count += prefix_map[prefix_sum - K]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count

# Example usage
arr = [10, 2, -2, -20, 10]
K = -10
result = count_subarrays_with_sum_k(arr, K)
print(result)  # Output: 3 (subarrays: [10, 2, -2, -20], [2, -2, -20, 10], [-20, 10])

#######################################
# no of subarray with exactly 'k' odd number

def count_subarrays_with_exactly_k_odds(arr, K):
    # Transform array: Replace even with 0 and odd with 1
    binary_arr = [1 if num % 2 != 0 else 0 for num in arr]
    
    prefix_sum = 0
    prefix_map = {}
    count = 0

    for num in binary_arr:
        prefix_sum += num

        if prefix_sum == K:
            count += 1

        if (prefix_sum - K) in prefix_map:
            count += prefix_map[prefix_sum - K]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count

# Example usage
arr = [1, 2, 1, 2, 1]
K = 2
result = count_subarrays_with_exactly_k_odds(arr, K)
print(result)  # Output: 4

