# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        #无脑dfs
        # if root == None:
        #     return 0
        # if self.isBST(root, -0x3f3f3f3f, 0x3f3f3f3f) == True:
        #     return self.cnt(root)
        # return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
        if root == None:
            return 0
        if self.isBST(root,-float('inf'),float('inf')):
            return self.cnt(root)
        else:
            return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))


    def isBST(self, root, L, R):    #判断一棵树是否为BST
        if root == None:
            return True
        if root.val <= L or root.val >=R:
            return False
        return self.isBST(root.left,L,root.val) and self.isBST(root.right,root.val,R)

    def cnt(self, root):       #统计树的结点个数
        if root == None:
            return 0
        return self.cnt(root.left) + self.cnt(root.right) + 1

