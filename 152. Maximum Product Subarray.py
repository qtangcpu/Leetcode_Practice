class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxNum = float("-inf")
        # imax, imin = 1, 1
        # for num in nums:
        #     if num < 0:
        #         imax,imin = imin,imax
        #     imax, imin = max(imax*num, num), min(imin*num, num)
        #     maxNum = max(maxNum, imax)
        # return maxNum

        ans = float('-inf')
        imax, imin = 1,1
        for num in nums:
            if num <0:
                imax,imin = imin, imax
            imax, imin = max(imax*num,num), min(imin*num,num)
            ans = max(ans,imax)
        return ans