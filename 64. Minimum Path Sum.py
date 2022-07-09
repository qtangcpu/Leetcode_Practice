'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for row in range(1, m):
            grid[row][0] = grid[row][0] + grid[row - 1][0]
        for col in range(1, n):
            grid[0][col] = grid[0][col] + grid[0][col - 1]

        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = min(grid[row - 1][col], grid[row][col - 1]) + grid[row][col]

        return grid[m - 1][n - 1]