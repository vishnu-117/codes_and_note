class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        result = []
        digit_mapping = {
            "1": "1",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "0"
        }
        def backtrack(index, current_str):
            if len(current_str) == len(A):
                result.append(current_str)
                return 
            
            for i in digit_mapping[A[index]]:
                backtrack(index+1, current_str + i)

        if len(A) > 1:
            backtrack(0, "")
        elif len(A) == 1:
            for i in  digit_mapping[A[0]]:
                result.append(i)
        return result
		
obj = Solution()
result = obj.letterCombinations("23")
print(result)
