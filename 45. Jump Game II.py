class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MaxPos, end, step = 0, 0, 0

        for i in range(n-1):
            if MaxPos >= i :
                MaxPos = max(MaxPos, i + nums[i])
                if end == i:
                    end = MaxPos
                    step +=1
        return step
