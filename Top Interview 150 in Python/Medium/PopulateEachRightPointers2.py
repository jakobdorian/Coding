"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Time Complexity: O(N), where N is the number of nodes in the binary tree. This is because each node is processed exactly once in the level order traversal.

# Space Complexity: O(W), where W is the maximum width of the tree (number of nodes in the widest level). In the worst case, the queue can contain all nodes in the widest level of the tree.


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # check if the tree is empty
        if not root:
            return None
        
        # initialize a deque for level order traversal
        q = deque()
        q.append(root)

        # perform level order traversal
        while q:
            curr, nxt = None, None

            # process all nodes in the current level
            for _ in range(len(q)):
                # handle the first node in the pair
                if not curr:
                    curr = q.popleft()

                    # add left and right children to the queue if they exist
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                # handle the second node in the pair
                elif not nxt:
                    nxt = q.popleft()
                    
                    # connect the current node to the next node
                    curr.next = nxt

                    # add left and right children of the next node to the queue
                    if nxt.left:
                        q.append(nxt.left)
                    if nxt.right:
                        q.append(nxt.right)
                # update the 'next' pointers and enqueue the next pair
                else:
                    curr = q.popleft()
                    nxt.next = curr

                    # add left and right children of the current node to the queue
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    nxt = curr

        # return the modified root of the tree with the 'next' pointers connected
        return root
