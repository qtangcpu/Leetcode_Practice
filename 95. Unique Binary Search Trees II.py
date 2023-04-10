# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def backtrack(l,r):
            if l >r :
                return [None]
            ans = []

            for i in range(l,r+1):
                left_trees = backtrack(l,i-1)
                right_trees = backtrack(i+1,r)
                for l_t in left_trees:
                    for r_t in right_trees:
                        curTree = TreeNode(i)
                        curTree.left = l_t
                        curTree.right = r_t
                        ans.append(curTree)
            return ans
        return backtrack(1,n)