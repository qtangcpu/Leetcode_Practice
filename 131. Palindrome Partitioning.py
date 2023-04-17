class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        self.isPalindrome = lambda x: x == x[::-1]

        def backtrack(ans,cur,s):
            if not s:
                ans.append(cur)
                return
            for i in range(1,len(s)+1):
                if self.isPalindrome(s[:i]):
                    backtrack(ans,cur+[s[:i]],s[i:])
        ans = []
        cur = []
        backtrack(ans,cur,s)
        return ans