class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n1 = len(text1)
        n2 = len(text2)

        matrix = [[0]*(n1+1 )for i in range(n2+1)]

        for i in range(1,n2+1):
            for j in range(1,n1+1):
                if text1[j-1] == text2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])

        return matrix[-1][-1]