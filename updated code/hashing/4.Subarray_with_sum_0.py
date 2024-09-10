def is_exist_subarray_with_sum_zero(arr):
    """
     O(n), TC: O(n)
    """
    prefix_sum = 0
    prefix_set = set()

    for num in arr:
        prefix_sum += num

        if prefix_sum == 0 or prefix_sum in prefix_set:
            return True
        
        prefix_set.add(prefix_sum)
    
    return False

# Example usage
arr = [4, 2, -3, 1, 6]
result = is_exist_subarray_with_sum_zero(arr)
print(result)

################################################
# To count the number of subarrays whose sum is zero

def count_subarrays_with_sum_zero(arr):
    prefix_sum = 0
    prefix_count = {}
    count = 0

    for num in arr:
        prefix_sum += num

        if prefix_sum == 0:
            count += 1
        
        if prefix_sum in prefix_count:
            count += prefix_count.get(prefix_sum)
        
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count

# Example usage
arr = [4, 2, -3, 1,6,-6,2,-3,1]
result = count_subarrays_with_sum_zero(arr)
print(result)  # Output: 4
