"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hashmap to map old nodes, with null pointing to null
        res = {None : None}

        curr = head
        while curr:
            # deep copy
            copy = Node(curr.val)
            # old node
            res[curr] = copy
            # update current
            curr = curr.next

        curr = head
        # set the pointers
        while curr:
            # get deep copy
            copy = res[curr]
            copy.next = res[curr.next]
            copy.random = res[curr.random]
            # update current
            curr = curr.next
        # return head
        return res[head]
