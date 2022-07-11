'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = {}
        col = {}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in row:
                        row[i] = True
                    if j not in col:
                        col[j] = True
        for key in row.keys():
            for j in range(n):
                matrix[key][j] = 0
        for key in col.keys():
            for i in range(m):
                matrix[i][key] = 0

        return matrix