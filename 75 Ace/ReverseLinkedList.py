class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a pointer to keep track of the previous node, initially set to None.
        prev = None
        # set the current pointer to the head of the linked list.
        curr = head

        # iterate through the linked list until the current pointer reaches the end (None).
        while curr:
            # store the next node in the list temporarily.
            temp = curr.next
            # reverse the link of the current node to point to the previous node.
            curr.next = prev
            # move the prev pointer to the current node.
            prev = curr
            # move the current pointer to the next node.
            curr = temp
        
        # return the new head of the reversed linked list (which is the last node of the original list).
        return prev
