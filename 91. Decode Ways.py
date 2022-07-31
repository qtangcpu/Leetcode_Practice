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