class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first use for loop to walk through all nums as the first side.
        # then use binary search to find the first num that is larger than nums[i]+nums[j]
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                l,r, k = j+1, n-1,j
                while l <= r:
                    mid = (l+r)//2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        l = mid + 1
                    else:
                        r = mid - 1
                print(k-j)
                ans += k - j
        return ans