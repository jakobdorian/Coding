# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node
        res = ListNode(0, head)
        # use two pointers
        left = res
        right = head
        # keep shifting right, until n == 0
        while n > 0 and right:
            right = right.next
            n -= 1
        # keep shifting both pointers until right reaches end of list
        while right:
            left = left.next
            right = right.next

        # remove node
        left.next = left.next.next
        return res.next
