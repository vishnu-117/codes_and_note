from typing import List

class Solution:
    """
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    """
    def letterCombinations(self, digits: str) -> List[str]:
        data = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno',
                7: 'pqrs', 8:'tuv', 9:'wxyz'}
        
        def dfs(index, tmp_str):
            if len(tmp_str) == len(digits):
                print(tmp_str)
                res.append(tmp_str)
                return
            
            for c in data[int(digits[index])]:
                dfs(index+1, tmp_str + c)

        res = []
        if digits:
            dfs(0, "")
        
        return res


obj = Solution()

print(obj.letterCombinations('23'))

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""