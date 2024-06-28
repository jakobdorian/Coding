class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # a list to keep track of the number of roads connected to each city
        edge_count = [0] * n
        res = 0
        
        # start with the smallest importance label
        label = 1

        # count the number of roads connected to each city
        for n1, n2 in roads:
            edge_count[n1] += 1
            edge_count[n2] += 1
        
        # sort the edge counts
        for count in sorted(edge_count):
            # add the current importance label multiplied by the number of roads to the result
            res += label * count
            # increment the importance label for the next city
            label += 1
        
        # return the total importance
        return res
