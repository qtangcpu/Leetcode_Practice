class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #step1: by doing seach on matrix[:][0] to see which row this number should be in
        #step2: search in this row
        if target > matrix[-1][-1]:
            return False
        if target < matrix[0][0]:
            return False

        f_r = [matrix[i][0] for i in range(len(matrix))]
        l = 0
        r = len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            if target == f_r[mid]:
                return True
            elif f_r[mid] > target:
                r = mid -1
            else:
                l = mid +1
        print(r)
        f_c = [matrix[r][j] for j in range(len(matrix[0]))]
        l = 0
        r = len(matrix[0])-1

        while l<=r:
            mid = (l+r)//2
            if target == f_c[mid]:
                return True
            elif f_c[mid] > target:
                r = mid -1
            else:
                l = mid +1
        return False
