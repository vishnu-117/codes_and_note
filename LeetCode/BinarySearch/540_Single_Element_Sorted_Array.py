class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # result = 0
        # for i in nums:
        #     result = result ^ i
        # return result
        
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if mid % 2 != 0:
                mid -= 1
            
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""