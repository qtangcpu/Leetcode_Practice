# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def backtrack(root,s,targetSum):
            if not root:
                return False
            s += root.val
            if s == targetSum and not root.left and not root.right:
                return True
            #elif s > targetSum:
            #    return False
            else:
                return backtrack(root.left,s,targetSum) or backtrack(root.right,s,targetSum)
        return backtrack(root,0,targetSum)