class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #(1+n)*n/2
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left