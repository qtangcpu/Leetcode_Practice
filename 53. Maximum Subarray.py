class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = - float('inf')
        temp = 0

        for i in range(len(nums)):
            temp += nums[i]
            res = max(temp,res)
            if temp < 0:
                temp = 0
        return res
