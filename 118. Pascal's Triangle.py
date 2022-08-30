class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return None
        if numRows == 1:
            return [[1]]
        ans = [[1] for i in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                ans[i].insert(j, ans[i - 1][j - 1] + ans[i - 1][j])
            ans[i].append(1)
        return ans
