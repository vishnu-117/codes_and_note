class Solution:
    def permute(self, s):
        result = []

        s = sorted(s)

        def backtrack(tmp_arr, frequency_arr):

            if len(tmp_arr) == len(s):
                result.append("".join(tmp_arr.copy()))
                return

            for i in range(len(s)):
                if frequency_arr[i] or (i > 0 and s[i] == s[i-1] and not frequency_arr[i-1]):
                    continue

                frequency_arr[i] = True
                tmp_arr.append(s[i])
                backtrack(tmp_arr, frequency_arr)
                tmp_arr.pop()
                frequency_arr[i] = False


        used = [False] * len(s)
        backtrack([], used)
        return result


obj = Solution()
print(obj.permute('aac'))

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        """
        Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations.

        input:
        A = [1, 1, 2]

        output:
        [ [1,1,2]
        [1,2,1]
        [2,1,1] ]
        """

        count = {n:0 for n in A}
        for i in A:
            count[i] += 1
        result = []
        tmp = []

        def dfs():
            if len(tmp) == len(A):
                result.append(tmp.copy())
                return

            for n in count:
                if count[n] > 0:
                    tmp.append(n)
                    count[n] -= 1
                    dfs()
                    tmp.pop()
                    count[n] += 1
        dfs()
        return result

obj = Solution()
print(obj.permute([1,2,2]))

