# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def b(pre_left,pre_end,in_left,in_end):
            if pre_left >pre_end:
                return None
            pre_root = pre_left
            in_root = index[preorder[pre_root]]
            left_size = in_root - in_left
            root = TreeNode(preorder[pre_root])

            root.left = b(pre_left+1,pre_left + left_size,in_left,in_root-1)
            root.right = b(pre_left+left_size+1,pre_end,in_root+1,in_end)
            return root
        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        return b(0, n - 1, 0, n - 1)