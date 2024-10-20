def generateParenthesis(open_count, close_count, tmp, result):
    """
    Generate all Parentheses II
    
    Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.

    input:
    A = 3

    output:
    [ "((()))", "(()())", "(())()", "()(())", "()()()" ]
    """
    if open_count == 0 and close_count == 0:
        result.append(tmp)
        return
    
    if open_count != 0:
        # tmp += "("
        generateParenthesis(open_count-1, close_count, tmp+"(", result)
    
    if close_count > open_count:
        # tmp += ")"
        generateParenthesis(open_count, close_count-1, tmp+")", result)

open_count = 4
close_count = 4
tmp = ""
result = []
generateParenthesis(open_count, close_count, tmp, result)
print(result)



################################
# other solution
################################
class Solution:
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, A):
		result = []
		stack = []
		def backtract(Open, Close):
			if Open == Close == A:
				result.append("".join(stack))
				return
			
			if Open < A:
				stack.append('(')
				backtract(Open + 1, Close)
				stack.pop()
			
			if Close < Open:
				stack.append(')')
				backtract(Open, Close + 1)
				stack.pop()
		backtract(0, 0)
		return result


