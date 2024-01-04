# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # curr = head
        # while curr:
        #     nxt = curr.next
        #     if curr.next:
        #         if nxt.val == val:
        #             curr.next = nxt.next
        #     else:
        #         curr.nxt = None

        #     curr = curr.next

        # return head

        if not head: return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

        