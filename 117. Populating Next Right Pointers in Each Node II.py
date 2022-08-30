"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        def bfs(curlayer):
            nextlayer = []
            for root in curlayer:
                if root.left:
                    nextlayer.append(root.left)
                if root.right:
                    nextlayer.append(root.right)
            for i in range(0, len(curlayer) - 1):
                curlayer[i].next = curlayer[i + 1]
            if len(nextlayer) >= 1:
                bfs(nextlayer)
            else:
                return
            return

        bfs([root])
        return root