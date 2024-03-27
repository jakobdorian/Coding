class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # slow and fast pointers to the head of the linked list
        slow, fast = head, head
        prev = None
        res = 0

        # loop until fast pointer reaches the end or the node before the end
        while fast and fast.next:
            # move fast pointer by two nodes and slow pointer by one node
            fast =  fast.next.next
            # temporarily store the next node of slow pointer
            temp = slow.next
            # reverse the link of slow pointer
            slow.next = prev
            # move prev pointer to current slow node
            prev = slow
            # move slow pointer to the stored next node
            slow = temp


        # iterate through the remaining part of the linked list
        while slow:
            # calculate the sum of values of the current pair and update res if needed
            res = max(res, prev.val + slow.val)
            # move prev and slow pointers to the next nodes
            prev = prev.next
            slow = slow.next
        
        # return the maximum sum found
        return res
