class Solution:
    """
    Given an array of candidate numbers A and a target number B, find all unique combinations in A where the candidate numbers sums to B.
    The same repeated number may be chosen from A unlimited number of times.

    Note:

    1) All numbers (including target) will be positive integers.

    2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).

    3) The combinations themselves must be sorted in ascending order.

    4) CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR ... (a1 = b1 AND a2 = b2 AND ... ai = bi AND ai+1 > bi+1)

    5) The solution set must not contain duplicate combinations.

    input:
    A = [2, 3, 6, 7]
    B = 7

    output:
    [ [2, 2, 3] , [7] ]
    """
    def combinationSum(self, A, B):
        result = []
        A = list(set(A))
        A.sort()
        def dfs(i, tmp, total):

            if total == B:
                result.append(tmp.copy())
                return
            
            if i >= len(A) or total > B:
                return
            
            tmp.append(A[i])
            dfs(i, tmp, total+A[i])
            tmp.pop()

            dfs(i+1, tmp, total)
        
        dfs(0, [], 0)
        return result

obj = Solution()
print(obj.combinationSum([2,3,6,7],7))