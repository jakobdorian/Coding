class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case: if the list is empty or has only one element, it is already sorted
        if not head or not head.next:
            return head

        # find the middle of the linked list using the helper function
        left = head
        right = self.helper(head)
        temp = right.next
        right.next = None
        right = temp

        # recursively sort the left and right halves of the linked list
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the sorted left and right halves
        return self.merge(left, right)

    def helper(self, head):
        # helper function to find the middle of the linked list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def merge(self, l, r):
        # helper function to merge two sorted linked lists
        tail = temp = ListNode()
        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        # if there are remaining elements in either list, append them to the merged list
        if l:
            tail.next = l
        if r:
            tail.next = r
        return temp.next
