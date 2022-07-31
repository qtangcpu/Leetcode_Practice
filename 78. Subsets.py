class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]

        def backtrack(start, current):
            for i in range(start, len(nums)):
                current.append(nums[i])
                ans.append(current[:])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return ans