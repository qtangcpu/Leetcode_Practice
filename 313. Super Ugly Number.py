class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [0] * (n)
        m = len(primes)
        pointers = [0] * m
        cur_nums = [1] * m
        for i in range(n):
            min_num = min(cur_nums)
            dp[i] = min_num
            for j in range(m):
                if cur_nums[j] == min_num:
                    pointers[j] += 1
                    cur_nums[j] = dp[pointers[j] - 1] * primes[j]

        return dp[-1]