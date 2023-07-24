class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if arr[0] > k:
            return k

        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) >> 1
            x = arr[mid] if mid < len(arr) else 10 ** 9
            if x - mid - 1 >= k:
                r = mid
            else:
                l = mid + 1

        return k + l