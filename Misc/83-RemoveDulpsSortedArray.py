# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start with the head of the list
        curr = head
        
        # traverse through the linked list
        while curr:
            # check if the next node exists and has the same value as the current node
            while curr.next and curr.next.val == curr.val:
                # if yes, skip the next node by pointing to the node after next
                curr.next = curr.next.next
            
            # move to the next node
            curr = curr.next
        
        # return the modified list starting from the head
        return head
        