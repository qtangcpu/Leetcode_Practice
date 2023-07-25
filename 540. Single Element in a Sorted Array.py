class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #总的数量一定是奇数个
        #偶数 mid 偶数
        #判断mid的同一个在前面还是后面
        #如果在前面说明缺失的后面： l = mid+1
        #如果在后面说明缺失的前面： r = mid-1
        #这个判断前面后面的方法不对
        #else mid就是那个数
        n = len(nums)
        l = 0
        r = n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]!= nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            elif nums[mid] == nums[mid-1]:#相等的在前面
                if (mid-1-l)%2 == 0:#前面偶数个说明在后面
                    l = mid+1
                else:
                    r = mid -2
            else:#相等的在后面
                if (mid-l)%2 == 0: #前面偶数个说明在后面
                    l = mid+2
                else:
                    r = mid -1

        return nums[l]