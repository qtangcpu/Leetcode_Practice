class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        # 初始化栈
        stack = []
        # 先存入第一项
        stack.append([s[0], 1])
        # 开始遍历
        for i in range(1, len(s)):
            # 如果栈不为空，且该项和栈顶元素相同
            if stack and s[i] == stack[-1][0]:
                # 则栈顶元素个数加1
                stack[-1][1] += 1
            else: # 否则把该元素加入到栈中
                stack.append([s[i], 1])
            # 如果栈顶元素的个数等于k,则直接弹出
            if stack[-1][1] == k:
                stack.pop()

        # 拼接最后栈中剩余元素作为输出
        for j in stack:
            for _ in range(j[1]):
                res += j[0]
        return res