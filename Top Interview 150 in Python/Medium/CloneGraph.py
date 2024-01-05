"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # dictionary to keep track of visited nodes and their corresponding clones
        visited = {}
        # dfs function to recursively clone the graph
        def dfs(node):
            # if the node has already been visited, return its clone
            if node in visited:
                return visited[node]
            # create a new node with the same value as the current node
            copy = Node(node.val)
            # store the mapping of original node to its clone in the visited dictionary
            visited[node] = copy
            # recursively clone the neighbors of the current node
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)
        