
class Solution:
    def uniqueSubsets(self, nums):
        nums.sort()  # Sort the array to handle duplicates
        result = []

        def backtrack(start, current_subset):
            # Add the current subset to the result
            result.append(current_subset.copy())
            
            for i in range(start, len(nums)):
                # Skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                # Recurse with the next index
                backtrack(i + 1, current_subset)
                # Backtrack
                current_subset.pop()

        # Start backtracking with an empty subset
        backtrack(0, [])

        return result

# Example usage
obj = Solution()
print(obj.uniqueSubsets([1, 2, 2]))

# class Solution:
#     # @param A : list of integers
#     # @return a list of list of integers
#     def unique_subset(self, A):
#         """
#         """
#         frequency_dict = {n:0 for n in A}
#         for i in A:
#             frequency_dict[i] += 1
#         tmp = []
#         result = []
#         frequency = []

#         for key, value in frequency_dict.items():
#             frequency.append((key, value))

#         def dfs(index, frequency, tmp):
#             if index == len(frequency):
#                 arr = []
#                 count = 0
#                 for i in frequency:
#                     arr.extend([i[0]]*tmp[count])
#                     count += 1
#                 result.append(arr.copy())
#                 return
#             for n in range(0, frequency[index][1]+1):
#                 tmp.append(n)
#                 dfs(index+1, frequency, tmp)
#                 tmp.pop()
#         dfs(0, frequency, tmp)
#         return result

# obj = Solution()
# print(obj.unique_subset([1,2,2]))

