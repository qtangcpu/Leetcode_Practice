class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        if n == 4 and sum(nums) == target:
            return [nums]
        ans = []

        for i in range(n - 3):
            next_target = target - nums[i]
            # if next_target <=0:
            #     return ans
            for j in range(i + 1, n - 2):
                next_next_target = next_target - nums[j]
                # if next_next_target <=0:
                #     break
                l = j + 1
                r = n - 1
                while l < r:
                    if nums[l] + nums[r] == next_next_target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < next_next_target:
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                    else:
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
        final_ans = []
        for a in ans:
            if a not in final_ans:
                final_ans.append(a)
        return final_ans


class Solution:
    def fourSum(self, nums, target):
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets

        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets


