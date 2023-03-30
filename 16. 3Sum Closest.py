class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # comparitively, we are looking for the the colest two sum
        n = len(nums)
        nums.sort()
        gap = 2**32-1
        if n == 3:
            return sum(nums)


        for i in range(0,n-2):
            l = i+1
            r = n-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                elif nums[i] + nums[l] + nums[r] < target:
                    if abs(nums[i] + nums[l] + nums[r] - target) < abs(gap):
                        gap = nums[i] + nums[l] + nums[r] - target
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    l+=1
                else:
                    if abs(nums[i] + nums[l] + nums[r] - target) < abs(gap):
                        gap = nums[i] + nums[l] + nums[r] - target
                    while l <r and nums[r] == nums[r-1]:
                        r -=1
                    r-=1
        return target + gap