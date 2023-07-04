class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        # just doing backwards
        # to decode we want to take this problem or not
        n = len(questions)
        dp = [0]*len(questions)
        dp[-1] = questions[-1][0]
        for i in range(len(questions)-2,-1,-1):
            if i+questions[i][1]+1 < n :
                take = i+questions[i][1]+1
            else:
                take = 0
            dp[i] = max(questions[i][0]+dp[take], dp[i+1])
        return dp[0]