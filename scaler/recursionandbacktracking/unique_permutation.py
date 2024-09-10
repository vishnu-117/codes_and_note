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

