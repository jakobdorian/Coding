# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(n), where n is the number of nodes in the linked list
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0  # length of the linked list
        curr = head  # traverse the linked list
        self.head = head  # reference to the head of the linked list

        # calculate the length of the linked list
        while curr:
            curr = curr.next
            n += 1

        # recursive function to build the binary search tree
        def helper(start, end):
            # base case: If start index is greater than end index, return None
            if start > end:
                return None
            # calculate the middle index
            mid = (start + end) // 2
            # recursively build the left and right subtrees
            left = helper(start, mid - 1)
            # create the root node using the current linked list node
            root = TreeNode(self.head.val)
            # move to next node in linked list
            self.head = self.head.next
            root.left = left  # attach the left subtree
            root.right = helper(mid + 1, end)  # attach the right subtree

            return root
        return helper(0, n - 1)
