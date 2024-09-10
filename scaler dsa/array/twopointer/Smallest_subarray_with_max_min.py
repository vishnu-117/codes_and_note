"""
https://www.geeksforgeeks.org/smallest-subarray-containing-minimum-and-maximum-values/

Given an array A of size N. The task is to find the length of smallest subarray which contains both maximum and minimum values.

Examples: 

Input : A[] = {1, 5, 9, 7, 1, 9, 4}
Output : 2
subarray {1, 9} has both maximum and minimum value.

Input : A[] = {2, 2, 2, 2}
Output : 1
2 is both maximum and minimum here.
"""

# Smallest subarray containing minimum and maximum values
def find_smallest_subarray(array):
    import sys
    max_value = max(array)
    min_value = min(array)

    ans = sys.maxsize
    min_index = -1
    max_index = -1

    for index in range(len(array)):

        if array[index] == max_value:
            max_index = index
        
        if array[index] == min_value:
            min_index = index
        
        if min_index != -1 and max_index != -1:
            ans = min(ans, abs(max_index - min_index)+1)
    return ans

print(find_smallest_subarray([1, 5, 9, 7, 4, 9]))