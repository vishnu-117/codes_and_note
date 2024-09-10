from typing import List

class Solution:
	"""
	https://leetcode.com/problems/generate-parentheses/
	"""
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(open_count, close_count, tmp_str):
            if open_count == n and close_count == n:
                result.append(tmp_str)
                return

            if open_count >= close_count and open_count <= n:
                dfs(open_count+1, close_count, tmp_str+'(')
                dfs(open_count, close_count+1, tmp_str+')')
        
        dfs(0, 0, "")
        return result
        
obj = Solution()
print(obj.generateParenthesis(3))