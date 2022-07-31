# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
            return result

        ans = dfs(root)
        if len(ans) <= 1:
            return True
        for i in range(1, len(ans)):
            if ans[i] > ans[i - 1]:
                continue
            else:
                print(ans[i])
                return False
        return True