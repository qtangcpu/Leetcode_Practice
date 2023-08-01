class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # loop through all possible index in the string as endpoint, and the resulkt of the current end point value will be the max
        # value before it +1 or itself(ofcourse you have to be larger than the point before you)
        if not nums:
            return 0

        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        # d = []
        # for n in nums:
        #     if not d or n > d[-1]:
        #         d.append(n)
        #     else:
        #         l, r = 0, len(d) - 1
        #         loc = r
        #         while l <= r:
        #             mid = (l + r) // 2
        #             if d[mid] >= n:
        #                 loc = mid
        #                 r = mid - 1
        #             else:
        #                 l = mid + 1
        #         d[loc] = n
        # return len(d)