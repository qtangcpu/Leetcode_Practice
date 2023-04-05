class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        MaxPos, end, cur = 0, 0, 0
        n = len(nums)

        for i in range(n):
            if MaxPos >= i:
                MaxPos = max(MaxPos, i + nums[i])
                if MaxPos >= n - 1:
                    return True
                if i == end:
                    if end >= MaxPos:
                        return False
                    end = MaxPos

        return True
