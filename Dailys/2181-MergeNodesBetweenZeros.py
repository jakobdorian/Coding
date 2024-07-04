# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to simplify edge case handling
        dummy = ListNode(0)
        # variable to keep track of the sum of values between zeros
        curr = 0
        # pointer to build the new list
        temp = dummy

        # skip the initial zero node as per problem statement
        head = head.next

        # traverse the linked list
        while head:
            if head.val == 0:
                # when a zero node is encountered, add the current sum to the new list
                temp.next = ListNode(curr)
                # move the temp pointer to the new node
                temp = temp.next
                # reset the current sum for the next segment
                curr = 0
            else:
                # Accumulate the values between zeros
                curr += head.val
            
            # move to the next node
            head = head.next

        # return the next of dummy node which points to the head of the new list
        return dummy.next
