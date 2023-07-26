class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # so strcitly increasing and decreasing before and after a pivot point.
        # n >=3
        n = len(arr)
        if n < 3:
            return 0

        l = 0
        r = n - 1

        # 1 2 3 4 5 6 3 1
        # 给了mountain， 找出index of peak
        # mid 落在上山or 下山
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
                r = mid - 1
            else:
                l = mid + 1
        return l