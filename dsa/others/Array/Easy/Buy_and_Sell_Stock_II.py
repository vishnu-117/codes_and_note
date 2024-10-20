class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    122. Best Time to Buy and Sell Stock II


    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                max_profit += prices[i+1] -prices[i]
        return max_profit
        