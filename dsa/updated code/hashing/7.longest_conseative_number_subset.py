def longest_consecutive(arr):
    """
    T.C: O(n), S.C: O(n)
    """
    num_set = set(arr)
    max_count = 0

    for num in arr:

        if num - 1 not in num_set:
            tmp_num = num
            tmp_count = 1

            while tmp_num + 1 in num_set:
                tmp_num += 1
                tmp_count += 1
            
            max_count = max(max_count, tmp_count)
    return max_count

arr = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(arr)
print(result)  # Output: 4