class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # create a list of perfect squares that are less than n
        nums = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for num in nums:
                if i >= num:
                    dp[i] = min(dp[i], dp[i - num] + 1)
        return dp[-1]