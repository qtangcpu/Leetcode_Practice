# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        record = []
        def dfs(root):
            if not root:
                return
            record.append(root)
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        for i in range(1,len(record)):
            prev, curr = record[i - 1], record[i]
            prev.left = None
            prev.right = curr