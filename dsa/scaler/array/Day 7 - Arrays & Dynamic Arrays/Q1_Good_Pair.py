class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # https://www.scaler.com/academy/mentee-dashboard/class/8801/assignment/problems/11160/?navref=cl_pb_nv_tb
    def solve(self, A, B):
        tmp = set()
        for i in A:
            if B - i in tmp:
                return 1
            tmp.add(i)
        return 0
"""
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j
and (A[i] + A[j] == B). Check if any good pair exist or not.

A = [1,2,3,4]
B = 7
output: 1

A = [1,2,4]
B = 4

output: 0
"""