class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxSide = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                else:
                    if i ==0 or j ==0:
                        matrix[i][j] = 1
                        maxSide = max(1,maxSide)
                    else:
                        matrix[i][j] = min(int(matrix[i-1][j]),int(matrix[i-1][j-1]),int(matrix[i][j-1]))+1
                        maxSide = max(matrix[i][j],maxSide)
        return maxSide**2