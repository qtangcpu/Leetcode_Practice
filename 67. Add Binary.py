'''
Given two binary strings a and b, return their sum as a binary string.

'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = len(a)-1
        n2 = len(b)-1
        carry = 0
        ans = ""
        while n1 >=0 or n2 >=0:
            num1 = 0 if n1<0 else int(a[n1])
            num2 = 0 if n2<0 else int(b[n2])
            ans = str((num1+num2+carry)%2) + ans
            carry =  (num1+num2+carry)//2
            n1 -=1
            n2 -=1
        if carry == 1:
            ans = "1"+ans
            return ans
        else:
            return ans