class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        p = 10 ** 9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % p
        ans = 0
        for i in range(len(nums)):
            if nums[i] * 2 <= target:
                t = target - nums[i]
                # 找剩下的里面第一个最后一个比他小的
                l, r, k = i + 1, n - 1, i
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] <= t:
                        k = mid
                        l = mid + 1
                    else:
                        r = mid - 1
                ans += f[k - i]
            else:
                return ans % p
        return ans % p

        # 0 1  ---- 2 (0 01)
        # 0 1 2 ---- 4(0 01 02 012)
        # 0 1 2 3 ----  8(0 01 02 03 013 023 012 0123)
        # 0 1 2 3 4 ---- 16(0 01 02 03 04 014 024 034 01224 0134 0234 01234)