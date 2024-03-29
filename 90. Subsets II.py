class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def backtrack(nums,startIndex):
            res.append(path[:])
            for i in range(startIndex,len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        nums = sorted(nums)
        backtrack(nums,0)
        return res