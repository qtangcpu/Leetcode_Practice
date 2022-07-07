'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        li = [[0]*m for i in range(n)]
        li[0][0] = 1 if obstacleGrid[0][0] == 0 else 0 #starting from [0,0]

        for i in range(1,n):  #fulfill the first row,rest will be 0 if one of them will be 0
            if obstacleGrid[i][0] == 1:
                li[i][0] = 0
            else:
                li[i][0] = li[i-1][0]

        for i in range(1,m):    #fulfill the first col,rest will be 0 if one of them will be 0
            if obstacleGrid[0][i] == 1:
                li[0][i] = 0
            else:
                li[0][i] = li[0][i-1]

        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 1:
                    li[i][j] = 0
                else:
                    li[i][j] =li[i][j-1]+li[i-1][j]
        return li[-1][-1]
