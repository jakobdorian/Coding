class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # extract the two nodes from the first edge
        a, b = edges[0]
        
        # check the first node of the second edge
        # if it matches either of the nodes from the first edge, it must be the center
        if edges[1][0] == a or edges[1][1] == a:
            return a
        else:
            # otherwise, the second node from the first edge is the center
            return b
            