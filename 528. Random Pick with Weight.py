class Solution:

    def __init__(self, w):
        n = len(w)
        self.prefix_sum = [0] * n
        self.prefix_sum[0] = w[0]

        # 前缀和
        for i in range(1, n):
            self.prefix_sum[i] = self.prefix_sum[i-1] + w[i]
        print(self.prefix_sum)


    def pickIndex(self):
        seed = random.randint(1, self.prefix_sum[-1])
        index = bisect_left(self.prefix_sum, seed)
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()