class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        if n <=1:
            return s

        check_matrix = [[False] * n for i in range(n)]
        for i in range(n):
            check_matrix[i][i] = True
        max_L = 1
        start = 0
        for L in range(2,n):
            for i in range(n):
                j = i + L -1
                if i > n - L:
                    break
                if s[i] != s[j]:
                    check_matrix[i][j] = False
                else:
                    if L <= 3:
                        check_matrix[i][j] = True
                    else:
                        check_matrix[i][j] = check_matrix[i + 1][j - 1]
                if check_matrix[i][j] == True:
                    max_L = max(max_L,L)
                    start = i
        return s[start:start + max_L]