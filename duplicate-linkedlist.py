class Solution(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def deleteDuplicates(self, head):
        current = head
        while current is not None and current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
