def has_pair_with_sum_k(arr, K):
    """
    TC: O(n), SC: O(n)
    """
    seen = set()

    for num in arr:
        target = K - num

        if target in seen:
            return True

        seen.add(num)

    return False

# Example usage
arr = [10, 15, 3, 7]
K = 17
result = has_pair_with_sum_k(arr, K)
print(result)  # Output: True (because 10 + 7 = 17)
