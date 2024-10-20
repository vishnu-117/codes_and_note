class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):
        count = 0
        from math import sqrt

        def is_number(number):
            if number <= 1:
                return 0
            
            for k in range(2, int(sqrt(num))+1):
                if num % k == 0:
                    return 0
            return 1

        for num in A:
            count += is_number(num)

        return count

"""
"Primal Power" of an array is defined as the count of prime numbers present in it.
Given an array of integers A of length N, you have to calculate its Primal Power.

Input 1:

 A = [-6, 10, 12]

Input 2:

 A = [-11, 7, 8, 9, 10, 11]


Output 1:

 0
Output 2:

 2
"""