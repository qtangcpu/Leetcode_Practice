class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0] * (n + 1) for _ in range(m + 1)]	# row:0's col:1's
        for str in strs:
            #loop through backpack first since we care about order for subsets
            ones = str.count('1')
            zeros = str.count('0')
            #背包问题一步一步刷新我们要求的dp【i】【j】遍历背包容量且从后向前遍历！
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zeros][j-ones] +1)

        return dp[-1][-1]