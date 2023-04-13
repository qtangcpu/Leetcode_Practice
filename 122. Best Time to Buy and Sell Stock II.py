class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        ans = 0
        for i in range(1, n):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                ans += profit

        return ans