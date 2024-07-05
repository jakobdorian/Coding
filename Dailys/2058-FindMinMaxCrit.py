# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # helper function to determine if the current node is a critical point
        def helper(prev, curr, next):
            return (
                prev.val > curr.val < next.val or 
                prev.val < curr.val > next.val
            )
        
        # pointers to traverse the linked list
        prev, curr = head, head.next
        next = curr.next

        # variables to track minimum and maximum distances
        min_dist, max_dist = float("inf"), float("-inf")

        # variables to track the positions of critical points
        prev_crit = 0
        first_crit = 0
        i = 1  # index to keep track of the current node's position

        # traverse the linked list
        while next:
            # check if the current node is a critical point
            if helper(prev, curr, next):
                if first_crit:  # if this is not the first critical point
                    # update the maximum distance
                    max_dist = i - first_crit
                    # update the minimum distance
                    min_dist = min(min_dist, i - prev_crit)
                else:  # if this is the first critical point
                    first_crit = i
                # update the position of the previous critical point
                prev_crit = i

            # move the pointers to the next set of nodes
            prev, curr, next = curr, next, next.next
            i += 1
        
        # if no critical points were found, set distances to -1
        if min_dist == float("inf"):
            min_dist = -1
            max_dist = -1

        # return the minimum and maximum distances between critical points
        return [min_dist, max_dist]
        