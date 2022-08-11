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


        if not root:
            return root

        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])

        # 外层的 while 循环迭代的是层数
        while Q:

            # 记录当前队列大小
            size = len(Q)

            # 遍历这一层的所有节点
            for i in range(size):

                # 从队首取出元素
                node = Q.popleft()

                # 连接
                if i < size - 1:
                    node.next = Q[0]

                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # 返回根节点
        return root

        if not root:
            return root

        Q = [root]
        while len(Q) >0:
            size = len(Q)
            for i in range(size):
                node = Q.pop(0)
                if i < size -1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root
        """
        if not root:
            return root
        level_start = root

        while level_start.left:
            check_node = level_start
            while check_node:

                check_node.left.next = check_node.right

                if check_node.next:
                    check_node.right.next = check_node.next.left

                check_node = check_node.next

            level_start = level_start.left

        return root