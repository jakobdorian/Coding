# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sum = defaultdict(float)
        total = defaultdict(int)

        def dfs(node, height):
            # edge case
            if not node: 
                return 0
            # recursive step on each side
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)

            # calculate sum and total
            sum[height] += node.val
            total[height] += 1
        dfs(root, 0)
        res = []
        # calculate the average
        for i in range(len(sum)):
            res.append(sum[i] / total[i])
        # return average lvls
        return res
