class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2) != len(s3):
            return False
        if len(s1) == len(s2) == len(s3) == 0:
            return True
        col = len(s2) + 1
        row = len(s1) + 1
        dp = [[False]*col for i in range(row)]
        dp[0][0] = True
        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0:
                    dp[i][j] = ( dp[i-1][j] and s1[i-1] == s3[i+j-1] ) or ( dp[i][j-1] and s2[j-1] == s3[i+j-1] )
                elif i > 0:
                    dp[i][j] = ( dp[i-1][j] and s1[i-1] == s3[i+j-1] )
                elif j > 0:
                    dp[i][j] = ( dp[i][j-1] and s2[j-1] == s3[i+j-1] )
        return dp[-1][-1]