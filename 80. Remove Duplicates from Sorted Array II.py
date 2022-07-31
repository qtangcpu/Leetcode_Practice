class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solve(k):
            u = 0
            for x in nums:
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            return u
        return solve(2)