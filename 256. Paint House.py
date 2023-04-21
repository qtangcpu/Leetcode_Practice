class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        m = len(costs)

        for i in range(1,m):
            costs[i][0] = min(costs[i][0]+costs[i-1][1],costs[i][0]+costs[i-1][2])
            costs[i][1] = min(costs[i][1]+costs[i-1][0],costs[i][1]+costs[i-1][2])
            costs[i][2] = min(costs[i][2]+costs[i-1][0],costs[i][2]+costs[i-1][1])
        return min(costs[-1])