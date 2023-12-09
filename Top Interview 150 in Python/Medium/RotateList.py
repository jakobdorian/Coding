# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge cases
        if not head:
            return head
        
        length, tail = 1, head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        # is it a multiple?
        if k == 0:
            return head
        
        # rotate
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        # new head of linked list
        res = curr.next
        curr.next = None
        tail.next = head

        return res
