class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for i in range(rowIndex):
            last = 0
            for j in range(i+1):
                first = ans.pop(0)
                ans.append(first + last)
                last = first
            ans.append(1)
        return ans