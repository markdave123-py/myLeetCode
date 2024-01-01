# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        currSet = set()
        while curr:
            if curr not in currSet:
                currSet.add(curr)
                curr = curr.next
            else:
                return True

        return False
