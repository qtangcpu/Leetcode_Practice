'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        row = 1
        while row <m and matrix[row][0] <= target:
            row +=1
        #binary search in row-1 row
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if matrix[row-1][mid] == target:
                return True
            elif matrix[row-1][mid] > target:
                r = mid-1
            else:
                l=mid+1
        return False
