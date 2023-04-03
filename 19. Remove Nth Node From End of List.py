# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode()
        dummy.next = head
        new_cur = dummy

        for i in range(count - n):
            new_cur = new_cur.next

        new_cur.next = new_cur.next.next

        return dummy.next