class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def unique_subset(self, A):
        """
        """
        frequency_dict = {n:0 for n in A}
        for i in A:
            frequency_dict[i] += 1
        tmp = []
        result = []
        frequency = []

        for key, value in frequency_dict.items():
            frequency.append((key, value))

        def dfs(index, frequency, tmp):
            if index == len(frequency):
                arr = []
                count = 0
                for i in frequency:
                    arr.extend([i[0]]*tmp[count])
                    count += 1
                result.append(arr.copy())
                return
            for n in range(0, frequency[index][1]+1):
                tmp.append(n)
                dfs(index+1, frequency, tmp)
                tmp.pop()
        dfs(0, frequency, tmp)
        return result

obj = Solution()
print(obj.unique_subset([1,2,2]))

