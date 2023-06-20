class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # the max_len of palindrome subseq will only be great or equal to its subseq. So we can use dynamic programming
        # we can go several ways as long as the cell to its left, right and left-right already has a value, and the cell at the
        #top-right coner need to be filled at last.
        n = len(s)
        matrix = [[0]*n for i in range(n)]
        for i in range(n):
            matrix[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    matrix[i][j] = matrix[i+1][j-1] + 2
                else:
                    matrix[i][j] = max(matrix[i+1][j],matrix[i][j-1])
        return matrix[0][n - 1]
