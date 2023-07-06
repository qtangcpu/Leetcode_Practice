class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s[0] == '0': return 0
        if len(s) == 1: return 1
        dp = [0]*(len(s)+1)
        valid = set(str(i) for i in range(1,27))
        dp[0] = 1
        dp[1] = 1

        for i in range(1,len(s)):#s 长度，check位置，对应 dp记录i+1
            if s[i] not in valid: #0
                if s[i-1:i+1] not in valid:
                    return 0
                else:
                    dp[i+1] = dp[i-1]
            else:
                if s[i-1:i+1] in valid:
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]

        return dp[-1]