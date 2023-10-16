# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        current = res
        i = 0
        # iterate until empty
        while l1 or l2 or i:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new sum
            temp = v1 + v2 + i
            i = temp // 10
            temp = temp % 10
            current.next = ListNode(temp)

            # update pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next