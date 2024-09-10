def removeDuplicates(nums):
    lt = len(nums)
    k = 0
    removed_count = 0
    
    while k < (lt-1):
        if nums[k] == nums[k+1]:
            nums.remove(nums[k])
            removed_count += 1
            lt = len(nums)
        else:
            k += 1

    nums.extend(['_']*removed_count)
    unique_element_count = len(nums) - removed_count
    return unique_element_count, nums

print(removeDuplicates([1,1,2]))