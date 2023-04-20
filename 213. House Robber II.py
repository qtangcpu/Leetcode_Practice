class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==1:
            return nums[0]
        def rob_seg(nums):
            if not nums:
                return 0
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            return dp[-1]
        return max(rob_seg(nums[1:]),rob_seg(nums[:-1]))