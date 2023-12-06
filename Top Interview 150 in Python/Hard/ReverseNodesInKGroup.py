# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        prevGroup = res

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next
            # reverse group
            prev, curr = kth.next, prevGroup.next

            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            # reset
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
        # return head of res/dummy node
        return res.next
    # helper to function to get kth
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        