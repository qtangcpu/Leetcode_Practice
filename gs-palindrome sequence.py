class Solution(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = int(1e9 + 7)

        k = 5
        dp = [defaultdict(int) for _ in range(k + 1)]
        dp[0][""] = 1

        n = len(s)
        for i in range(n):
            c = s[i]
            for d in range(k + 1 - 1, 1 - 1, -1):
                for subStr, freq in dp[d - 1].items():
                    if d <= (k + 1) // 2 or (c == subStr[k - d]):
                        dp[d][subStr + c] += freq

        cnt = sum(dp[k].values())
        return cnt % mod



