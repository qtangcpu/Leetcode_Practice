# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = 10**9
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right))
        return min_depth+1