class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the transition condition is not simply certain ways, but we need to consider the diff condition at the ending two blocks,
        MOD = 10 ** 9 + 7
        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][3] = (((dp[i - 1][0] + dp[i - 1][1]) % MOD + dp[i - 1][2]) % MOD + dp[i - 1][3]) % MOD
        return dp[n][3]