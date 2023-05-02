# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            # 对于以结点 node 为根的子树：
            #   rob0: 不选结点 node 所能得到的最大权值和
            #   rob1: 选择结点 node 所能得到的最大权值和
            if node is None:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)

            rob0 = max(left) + max(right)
            rob1 = node.val + left[0] + right[0]

            return rob0, rob1

        res = dfs(root)

        return max(res)