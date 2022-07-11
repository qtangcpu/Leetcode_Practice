'''
You are climbing a staircase. It takes n steps to reach the top.
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        def backtrack(togo):
            if togo == 0:
                return 1
            elif togo ==1:
                return backtrack(togo-1)
            return backtrack(togo-1) + backtrack(togo-2)

        return backtrack(n)
        '''
        ans = [1, 2]
        if n <= 2:
            return n
        for i in range(2, n):
            ans.append(ans[i - 2] + ans[i - 1])
        return ans[-1]