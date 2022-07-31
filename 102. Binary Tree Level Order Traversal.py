# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        def traverse(root,level):
            if not root:
                return
            if level >= len(ans):
                ans.append([])
            ans[level].append(root.val)
            traverse(root.left,level+1)
            traverse(root.right,level+1)
            return
        traverse(root,0)
        return ans