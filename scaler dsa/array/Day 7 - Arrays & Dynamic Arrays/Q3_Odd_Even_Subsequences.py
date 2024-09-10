class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        
        next_odd = True if A[0] % 2 != 0 else False
        odd_even_count = 0

        for num in A:
            if (num % 2 != 0 and next_odd) or (num % 2 == 0 and not next_odd):
                odd_even_count += 1
                next_odd = not next_odd
        return odd_even_count

"""

Given an array of integers A of size, N. Find the longest subsequence of A, which is odd-even.

A subsequence is said to be odd-even in the following cases:

The first element of the subsequence is odd; the second element is even, the third element is odd, and so on.
For example: [5, 10, 5, 2, 1, 4], [1, 2, 3, 4, 5]

The first element of the subsequence is even, the second element is odd, the third element is even, and so on. 
For example: [10, 5, 2, 1, 4, 7], [10, 1, 2, 3, 4]

Return the maximum possible length of odd-even subsequence.

Note: An array B is a subsequence of an array A if B can be obtained from A by deleting several (possibly, zero, or all) elements.

Input 1:
    A = [1, 2, 2, 5, 6]
Output 1:
    4
    Explanation 1:
        Maximum length odd even subsequence is [1, 2, 5, 6]

Input 2:
    A = [2, 2, 2, 2, 2, 2]
Output 2:
    1
    Explanation 2:
        Maximum length odd even subsequence is [2]
"""
