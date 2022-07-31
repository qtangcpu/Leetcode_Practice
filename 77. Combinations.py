class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = list()

        def backtrack(current, k, start):
            if k == 0:
                ans.append(current[:])
            else:
                for i in range(start, n):
                    current.append(i + 1)
                    backtrack(current, k - 1, i + 1)
                    current.pop()

        backtrack([], k, 0)
        return ans