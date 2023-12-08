# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        
        c = Counter(temp)
        # only unique items
        temp = [k for k, v in c.items() if v == 1]

        # generate sorted linked list
        res = curr = ListNode()
        for i in temp:
            curr.next = ListNode(i)
            curr = curr.next
        
        # return the new head
        return res.next
