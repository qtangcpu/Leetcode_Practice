def deleteAndEarn(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #break this question down to to parts
    #part1: creat nums into multiple series that each can be calculated as the rob question
    #part2: sum the result of each rob question
    def rob(s):
        n = len(s)
        if n == 1:
            return s[0]
        first, second = s[0], max(s[0], s[1])
        for i in range(2, size):
            first, second = second, max(first + s[i], second)
        return second
    n = len(nums)
    nums.sort()
    ans = 0
    s = [nums[0]]
    for i in range(1,n):
        val = nums[i]
        if val == nums[i-1]:
            s[-1] +=val
        elif val == nums[i-1]+1:
            s.append(val)
        else:
            ans += rob(s)
            s = [val]
    ans += rob(s)
    return ans
