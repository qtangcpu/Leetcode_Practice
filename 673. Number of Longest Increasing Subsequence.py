class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # find the max_len problem, and cnt along the way

        dp = []
        cnt = []
        max_len = 0
        ans = 0
        for i in range(len(nums)):
            dp.append(1)
            cnt.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j]+1
                        cnt[i] = 1
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] +=1
            if dp[i] > max_len:
                max_len = dp[i]
                ans = cnt[j]
            elif dp[i] == max_len:
                ans += cnt[j]

        return ans
