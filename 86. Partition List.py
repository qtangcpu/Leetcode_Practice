# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        start = ListNode(-1)
        new_list = ListNode(-1)
        cur_new_list = new_list
        cur = start
        while head:
            if head.val <x:
                cur.next = head
                head = head.next
                cur = cur.next
            else:
                cur_new_list.next = head
                head = head.next
                cur_new_list = cur_new_list.next

        cur_new_list.next = None
        cur.next = new_list.next

        return start.next