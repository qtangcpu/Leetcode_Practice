class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        elif x > 0:
            result = min(int(str(x)[::-1]), 2 ** 31)

        else:
            result = -int(str(x)[1:][::-1])

        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0