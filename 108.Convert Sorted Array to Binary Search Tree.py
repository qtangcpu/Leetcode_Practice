# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def construct(start,end):
            if start>end:
                return None
            root_index = (start+end)//2
            root = TreeNode(nums[root_index])
            root.left = construct(start,root_index-1)
            root.right = construct(root_index+1,end)
            return root
        root = construct(0,len(nums)-1)
        return root