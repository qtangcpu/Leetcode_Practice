class Solution(object):
    def canWin(self, currentState):
        """
        :type currentState: str
        :rtype: bool
        """

        s = list(currentState)
        n = len(s)
        for i in range(n-1):
            if s[i] == "+" and s[i+1] == "+":
                s[i] = "-"
                s[i+1] = "-"
                if self.canWin(''.join(s)) == False:
                    return True
                s[i] = '+'
                s[i+1] = '+'
        return False