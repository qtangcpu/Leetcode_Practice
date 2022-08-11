# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(root,level):
            if not root:
                return
            if level>len(ans):
                ans.append([])
            dfs(root.left,level+1)
            dfs(root.right,level+1)
            ans[level-1].append(root.val)
            return

        dfs(root,1)
        return ans[::-1]