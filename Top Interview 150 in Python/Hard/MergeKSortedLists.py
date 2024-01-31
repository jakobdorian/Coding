class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # check if the input list of lists is empty
        if not lists:
            return None
        # if there is only one list in the input, return that list
        if len(lists) == 1:
            return lists[0]
        # helper function to merge two sorted linked lists
        def helper(l1, l2):
            dummy = curr = ListNode(0)  # dummy node to simplify list construction
            while l1 and l2:
                # compare values of the current nodes in l1 and l2
                if l1.val < l2.val:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                curr = curr.next  # move the pointer to the last node in the merged list
            # append the remaining nodes from either l1 or l2
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next  # return the merged list excluding the dummy node
        # initialize the result to the first list in the input
        res = lists[0]
        # merge the remaining lists one by one with the current result
        for l in lists[1:]:
            res = helper(res, l)
        return res
        