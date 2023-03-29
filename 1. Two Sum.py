class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in h:
                return [h[target - nums[i]],i]
            else:
                h[nums[i]] = i
