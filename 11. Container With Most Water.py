class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) # the number of vertical lines
        l = 0 # left pointer
        r = n-1 # right pointer
        cur_max = 0

        while l != r:
            # each time, we move the shorter lines
            cur_max = max(cur_max, (r-l)*min(height[l],height[r]))
            if height[l] >= height[r]:
                r -=1
            else:
                l +=1
        return cur_max
