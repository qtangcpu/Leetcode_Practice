# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def construct(post_start,post_end,in_start,in_end):
            if post_end<post_start:
                return None
            post_root = postorder[post_end]
            in_root_index = index[ postorder[post_end]]
            right_tree_size = in_end-in_root_index
            root = TreeNode(post_root)
            root.left = construct(post_start,post_end-right_tree_size-1,in_start,in_root_index-1)
            root.right = construct(post_end-right_tree_size,post_end-1,in_root_index+1,in_end)
            return root
        n = len(postorder)
        index = {element: i for i, element in enumerate(inorder)}
        return construct(0, n - 1, 0, n - 1)