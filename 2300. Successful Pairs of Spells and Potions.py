class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        #loop through each spells
        potions.sort()
        ans = []
        for i in range(len(spells)):
            l = 0
            r = len(potions)-1
            k = len(potions)
            target = success
            while l <= r:
                mid = (l+r)//2
                if potions[mid]*spells[i] >= target:
                    k = mid
                    r = mid-1
                else:
                    l = mid+1
            ans.append(len(potions)-k)
        return ans