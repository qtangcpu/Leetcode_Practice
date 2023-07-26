class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # first find the index to insert
        l = 0
        r = len(arr) - 1
        insert = r
        if len(arr) <= k:
            return arr
        while l < r:
            mid = (l + r) // 2
            if arr[mid] >= x:
                insert = mid
                print(insert)
                r = mid
            else:
                l = mid + 1

        pl = insert - 1
        pr = insert
        print(pr)
        for _ in range(k):
            if pl < 0:
                pr += 1
            elif pr >= len(arr) or x - arr[pl] <= arr[pr] - x:
                pl -= 1
            else:
                pr += 1

        return arr[pl + 1: pr]
