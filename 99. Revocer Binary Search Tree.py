# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        dfs(root)
        x = None
        y = None
        pre = nodes[0]
        for i in xrange(1,len(nodes)):
            if pre.val>nodes[i].val:
                y=nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]
        if x and y:
            x.val,y.val = y.val,x.val