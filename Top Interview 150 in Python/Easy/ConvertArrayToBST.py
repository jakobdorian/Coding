# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity: O(n), where n is the number of elements in the input array
# Space complexity: O(log n), where log n is the maximum depth of the recursion stack
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # helper function to recursively build a balanced BST
        def helper(left, right):
            # base case 
            if left > right:
                return None
            # calculate mid index to split the array
            mid = (left + right) // 2
            # create a TreeNode with the value of the middle element
            root = TreeNode(nums[mid])
            # recursively build left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root
        return helper(0, len(nums) - 1)
