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

        # ans = []
        #
        # for i in range(numRows + 1):
        #     for j in range(i):
        #         if j == 0:
        #             ans.append([1])
        #         elif j == i - 1:
        #             ans[-1].append(1)
        #         else:
        #             ans[-1].append(ans[-2][j - 1] + ans[-2][j])
        #
        # return ans
