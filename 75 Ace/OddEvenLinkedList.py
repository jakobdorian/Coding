class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check if the linked list is empty or contains only one or two nodes
        if not head or not head.next or not head.next.next:
            return head

        # initialize pointers for odd nodes, even nodes, and the head of even nodes
        odd, even, evenhead = head, head.next, head.next
        curr = head  # a pointer to traverse the linked list
        i = 1  # a counter for tracking the position of nodes

        # traverse the linked list
        while curr:
            # for nodes beyond the second position, update odd and even nodes alternatively
            if i > 2 and i % 2 != 0:
                odd.next = curr
                odd = odd.next
            elif i > 2 and i % 2 == 0:
                even.next = curr
                even = even.next
            curr = curr.next  # move to the next node
            i += 1  # increment the counter

        even.next = None  # terminate the even list
        odd.next = evenhead  # connect the odd list with the head of even list

        return head  # return the modified head of the linked list
