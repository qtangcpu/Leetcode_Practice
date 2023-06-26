class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # f[i][0]: does not hold. f[i][1] hold
        n = len(prices)
        dp = [[0,-prices[0]]]+ [[0,0] for i in range(n-1)]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return dp[n - 1][0]