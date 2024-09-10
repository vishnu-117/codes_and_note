import sys
# ===========================================
# DP SOLUTION
# ===========================================
def min_coin(arr, target):
    dp = [sys.maxsize] * (target + 1)
    dp[0] = 0

    def minCoins(target):
        if target < 0:
            return sys.maxsize
        
        if dp[target] != sys.maxsize:
            return dp[target]

        for coin in arr:
            dp[target] = min(dp[target], 1 + minCoins(target - coin))
        
        return dp[target]

    result = minCoins(target)
    return result if result != sys.maxsize else -1

print(min_coin([5,10,25], 30))
# ===============================
# RECURSIVE SOLUTION
# ===============================
def min_coin(arr, target):
    min_coin_count = sys.maxsize

    def dfs(index, tsum, count):
        nonlocal min_coin_count
        if tsum > target:
            return

        if tsum == target:
            min_coin_count = min(min_coin_count, count)
            return

        if index >= len(arr):
            return

        # Choose the current coin
        dfs(index, tsum + arr[index], count + 1)

        # Do not choose the current coin and move to the next
        dfs(index + 1, tsum, count)

    dfs(0, 0, 0)
    return min_coin_count if min_coin_count != sys.maxsize else -1  # Return -1 if no solution

print(min_coin([5, 10, 25], 30))  # Output: 2 (using coins 5 and 25)


# def min_coin(arr, target):
#     min_coin_count = sys.maxsize

#     def dfs(index, tsum, tmp):
#         nonlocal min_coin_count
#         if tsum > target or index >= len(arr):
#             return
        
#         if tsum == target:
#             min_coin_count = min(min_coin_count, len(tmp))
#             return

#         tmp.append(arr[index])
#         dfs(index, tsum+arr[index], tmp)
#         tmp.pop()

#         dfs(index+1, tsum, tmp)
    
#     dfs(0, 0, [])
#     return min_coin_count


# print(min_coin([5,10,25], 30))

# def min_coin(arr, target):
#     min_coin_count = sys.maxsize
#     dp = [-1] * (len(arr) + 1)
#     ans = sys.maxsize

#     def bfs(target):
#         if target == 0: return 0
#         if target < 0: return sys.maxsize

#         if dp[target] != 1: return dp[target]

#         for i in range(len(arr)):
#             ans = min(ans, 1+bfs(target-arr[i]))
#             dp[i] = ans

#         return ans

#     bfs(target) 
#     return ans

