class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        # str_len = len(palindrome)
        # if str_len < 2:
        #     return ""
        # for idx in range(str_len >> 1):
        #     if palindrome[idx] > 'a':
        #         return palindrome[:idx] + 'a' + palindrome[idx+1:]
        # return palindrome[:str_len-1] + 'b'

        if len(palindrome) == 1:
            return ''
        s = list(palindrome)
        n, flag = len(s), False
        for i in range(n):
            if s[i] != 'a' and (n % 2 == 0 or n % 2 != 0 and i != n // 2):
                s[i] = 'a'
                flag = True
                break
        if not flag:
            s[-1] = 'b'

        return ''.join(s)