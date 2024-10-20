class Solution:
    """
    26. Remove Duplicates from Sorted Array
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l += 1
        return l