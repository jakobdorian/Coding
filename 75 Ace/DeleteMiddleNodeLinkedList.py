class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers, slow and fast, both pointing to the head of the linked list.
        slow, fast = head, head
        # pointer to keep track of the previous node.
        prev = None

        # traverse the linked list until either fast or fast.next becomes none.
        while fast and fast.next:
            # update prev to the current slow node.
            prev = slow
            # move slow one step forward.
            slow = slow.next
            # move fast two steps forward.
            fast = fast.next.next
        
        # if prev is not None, it means slow is not the head of the list.
        if prev:
            # skip the middle node by updating the next pointer of the previous node to point to the node after slow.
            prev.next = slow.next
        else:
            # if prev is None, it means the head itself was the middle node.
            # update the head to point to the node after slow.
            head = head.next
        
        # return the head of the updated linked list.
        return head
