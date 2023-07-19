# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l, r, x, y):
#        """
#        :type l, r, x, y: int
#        :rtype int
#        """
#
#	 # Returns the length of the array
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: integer
        """
        n = reader.length()
        L = 0               #实指
        R = n - 1           #实指
        while L < R :
            mid = L + R >> 1
            #-------------- 奇数个，L=0 [0 1 2] mid=3 [3 4 5 6] R=6
            if (R - L) % 2 == 0:
                #比较 [0 1 2] 和 [4 5 6]
                check = reader.compareSub(L, mid - 1, mid + 1 , R)
                #-- 左边大，在左
                if check == 1:
                    R = mid - 1     #左半的R界为mid=2
                #-- 右边大，在右
                elif check == -1:
                    L = mid + 1     #右半的L界为4
                #-- 两边一样大
                else:
                    return mid

            #--------------偶数个，L=0 [0 1 2] mid=2 [3 4 5] R=5
            else:
                #-- 比较 [0 1 2] 和 [3 4 5]
                check = reader.compareSub(L, mid, mid + 1, R)
                #-- 左边大，在左
                if check == 1:
                    R = mid         #左半的R界为2
                #-- 右边大，在右
                elif check == -1:
                    L = mid + 1     #右半的L界为3
                #-- 两边一样大，不存在
                else:
                    return -1
        return R