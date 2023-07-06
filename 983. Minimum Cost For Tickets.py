class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        size = len(days)
        maxDay= days[-1]
        dp = [0] * (maxDay + 31)
        daysSet = set(days)
        for d in range(maxDay, -1, -1):
            if d in daysSet:
                dp[d] = min(dp[d + 1] + costs[0], dp[d + 7] + costs[1], dp[d + 30] + costs[2])
            else:
                dp[d] = dp[d + 1]
        return dp[0]