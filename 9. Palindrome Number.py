class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x <0 or (x !=0 and x%10 == 0):
            return False
        a = x
        reversed_ = 0
        while x >0:
            reversed_ = reversed_*10 + x % 10
            x = x//10
        if a == reversed_:
            return True
        else:
            return False