class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #permulate through all possible diff in this array and use the same method we have for finding the longest subseq with a fixed diff.

        minv, maxv = min(nums), max(nums)
        diff = maxv - minv
        ans = 1

        for d in range(-diff,diff+1):
            f = defaultdict(int)
            for num in nums:
                f[num] = f[num-d]+1
            ans = max(ans,max(f.values()))
        return ans