def NoOfPair(n):
    """
    https://www.geeksforgeeks.org/number-of-ways-to-pair-people/
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + (i-1) * dp[i-2]

    return dp[n]

print(NoOfPair(4))

"""
Given that there are p people in a party. Each person can either join dance as a 
single individual or as a pair with any other. The task is to find the number of
different ways in which p people can join the dance.

Input : p = 3
Output : 4
Let the three people be P1, P2 and P3
Different ways are: {P1, P2, P3}, {{P1, P2}, P3},
{{P1, P3}, P2} and {{P2, P3}, P1}.

Input : p = 2
Output : 2
The groups are: {P1, P2} and {{P1, P2}}.
"""