# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # depth-first search function to traverse the tree and populate the result
        def dfs(node, level, res):
            # base case: If the node is none, return
            if not node:
                return 0
            
            # if the current level exceeds the length of the result list, add a new empty list
            if len(res) <= level:
                res += [[]]
            
            # recursively traverse the left and right subtrees
            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)

            # append or insert the node value based on the level's parity (zigzag pattern)
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
        
        # start the depth-first search from the root at level 0
        dfs(root, 0, res)
        return res
        