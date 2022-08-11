# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_b(root):
            if not root:
                return 0
            height = 1+ max(is_b(root.left),is_b(root.right))
            return height
        if not root:
            return True
        return abs(is_b(root.left)-is_b(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)