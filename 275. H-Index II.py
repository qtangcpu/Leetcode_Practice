class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # the largest index i that citations[i]- (i+1) <0
        # and return len(citations) - (i+1)
        n = len(citations)
        left = 0; right = n - 1
        while left <= right:
            mid = (left+right)//2
            if citations[mid] >= n-mid:
                right = mid -1
            else:
                left = mid +1
        return n-left