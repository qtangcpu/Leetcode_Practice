class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #当天持有股票 和 不持有股票
        #                 - 今天刚卖，明天进入冷冻期。- 之前就卖了
        # 第一天： 当天就有的话是-price， 0，0
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 当天持有股票
        # f[i][1]: 当天卖出股票
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])