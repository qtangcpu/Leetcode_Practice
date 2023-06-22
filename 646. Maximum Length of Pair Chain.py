class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # if we use dynamic programming, we just need to sort the pairs according to index0 for each pair
        n = len(pairs)
        pairs = sorted(pairs)
        record = []

        for i in range(n):
            record.append(1)
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    record[i] = max(record[j]+1, record[i])
        return max(record)

        # otherwise,m we can use greedy
        # therefore, we need to sort by index 1
        # cur, res = -inf, 0
        # for x, y in sorted(pairs, key=lambda p: p[1]):
        #     if cur < x:
        #         cur = y
        #         res += 1
        # return res