class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        n = len(s)
        d = {}
        def dfs(index):
            if index in d:
                return d[index]
            #字符串走到头了，返回1
            if index >= n:
                return 1
            a,b = 0,0
            #如果当前字符不是0开头的，则可以编码
            if s[index] != '0':
                a = dfs(index + 1)
            #如果当前字符不是0开头，并且跟下一个字符组合起来，小于等于26
            if index + 1 < n and s[index] != '0' and int(s[index] + s[index + 1]) <= 26:
                b = dfs(index + 2)
            d[index] = a + b
            return d[index]
        return dfs(0)


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': return 0
        if len(s) == 1: return 1

        legalstr = set(str(i) for i in range(1, 27))

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i] not in legalstr:  # 0
                if s[i - 1: i + 1] not in legalstr:
                    return 0
                else:
                    dp[i + 1] = dp[i - 2 + 1]  # 因为dp多了一个，所以集体加1
            else:
                if s[i - 1: i + 1] in legalstr:
                    dp[i + 1] = dp[i - 1 + 1] + dp[i - 2 + 1]
                else:
                    dp[i + 1] = dp[i - 1 + 1]
        return dp[-1]


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': return 0
        if len(s) == 1: return 1

        legalstr = set(str(i) for i in range(1, 27))

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i] not in legalstr:  # 0
                if s[i - 1: i + 1] not in legalstr:
                    return 0
                else:
                    dp[i + 1] = dp[i - 2 + 1]  # 因为dp多了一个，所以集体加1
            else:
                if s[i - 1: i + 1] in legalstr:
                    dp[i + 1] = dp[i - 1 + 1] + dp[i - 2 + 1]
                else:
                    dp[i + 1] = dp[i - 1 + 1]
        return dp[-1]