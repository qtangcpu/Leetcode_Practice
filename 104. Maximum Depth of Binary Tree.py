# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root,cur):
            if not root:
                self.ans = max(cur,self.ans)
                return
            dfs(root.left,cur+1)
            dfs(root.right,cur+1)
            return
        ans = dfs(root,0)
        return self.ans