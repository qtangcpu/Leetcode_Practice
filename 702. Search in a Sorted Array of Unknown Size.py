class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0

        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        # binary search
        left = 0
        while left <= right:
            # pivot = left + ((right - left) >> 1)
            pivot = (left + right) // 2
            num = reader.get(pivot)

            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1

        # there is no target element
        return -1