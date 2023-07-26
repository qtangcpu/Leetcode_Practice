class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        res = -1
        while l < r:
            while nums[r] >= k:
                r -= 1
            s = nums[l] + nums[r]
            if s >= k:
                r -= 1
            else:
                res = max(res, s)
                l += 1

        return res