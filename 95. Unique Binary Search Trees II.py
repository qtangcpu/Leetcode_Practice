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

        def generateTrees(start, end):
            if start > end:
                return [None]

            allTrees = []
            for i in range(start, end + 1):

                leftTrees = generateTrees(start, i - 1)
                rightTrees = generateTrees(i + 1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []