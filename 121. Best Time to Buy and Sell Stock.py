class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        minPrice = float('inf')
        maxPt = 0

        for price in prices:
            maxPt = max(maxPt, price - minPrice)
            minPrice = min(price, minPrice)

        return maxPt