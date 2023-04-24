class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n or not k: return 0

        same, diff = 0, k
        for i in range(1, n):
            same, diff = diff, (k - 1) * (same + diff)

        return same + diff
