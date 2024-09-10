def element_frequencies(arr):
    """
    TC:  O(n) , SC: O(n)
    """
    # Create an empty dictionary to store frequencies
    freq = {}

    # Iterate over each element in the array
    for num in arr:
        # Increment the frequency count of the current element
        freq[num] = freq.get(num, 0) + 1

    return freq

# Example usage
arr = [1, 2, 2, 3, 4, 4, 4, 5]
frequencies = element_frequencies(arr)

# Print the frequencies of each element
for element, count in frequencies.items():
    print(f"Element {element} appears {count} times")
