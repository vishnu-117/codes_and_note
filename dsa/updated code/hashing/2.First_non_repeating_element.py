def first_non_repeating_element(arr):
    """
    TC: O(n), SC: O(n)
    """
    freq = {}

    # Count the frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Find the first element with a frequency of 1
    for num in arr:
        if freq[num] == 1:
            return num

    # If no non-repeating element is found, return 0
    return 0

arr = [-1, 2, -1, 3, 2]
result = first_non_repeating_element(arr)
print(result)  # Output: 3
