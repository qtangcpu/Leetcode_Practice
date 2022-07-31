# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        for _ in range(left - 1):
            pre = pre.next


        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        left_node = pre.next
        curr = right_node.next
        right_node.next = None
        def reverse_linked_list(head):
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
        reverse_linked_list(left_node)
        pre.next = right_node
        left_node.next = curr
        return dummy_node.next