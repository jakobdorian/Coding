# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(n) sol
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge case, i.e., no change in linked list
        if left == right:
            return head
        
        res = ListNode(0, next=head)
        prev = res
        i = 1

        while i < left:
            prev = prev.next
            i += 1
        
        curr = prev.next
        nxt = curr.next

        while i < right:
            temp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = temp
            i += 1
        
        prev.next.next = nxt
        prev.next = curr

        return res.next
            