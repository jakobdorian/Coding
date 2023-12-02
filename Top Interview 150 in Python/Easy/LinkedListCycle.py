# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# floyd's tortoise and hare algo
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # while not null loop
        while fast and fast.next:
            # shift slow pointer by 1
            slow = slow.next
            # shift fast pointer by 2
            fast = fast.next.next
            # if they ever meet, return true
            if slow == fast:
                return True
        return False
