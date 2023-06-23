class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        #its a problem about the same numbers in two arrays and their order.

        n1 = len(nums1)+1
        n2 = len(nums2)+1
        matrix = [[0]*n1 for i in range(n2)]

        for i in range(1,n2):
            for j in range(1,n1):
                if nums1[j-1] == nums2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])


        return matrix[-1][-1]