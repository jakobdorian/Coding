class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Number of cities
        N = len(isConnected)
        
        # array to track visited cities
        visited = [False] * N

        # helper function to traverse connected cities from a starting point
        def helper(start):
            # queue for BFS traversal
            q = collections.deque()
            # add starting city to queue
            q.append(start)
            # mark starting city as visited
            visited[start] = True

            # perform BFS traversal
            while len(q) > 0:
                # get the current city from the queue
                curr = q.popleft()
                # traverse through all cities
                for i in range(N):
                    # if the current city is connected to city i and i is not visited
                    if isConnected[curr][i] and not visited[i]:
                        # add city i to the queue
                        q.append(i)
                        # mark city i as visited
                        visited[i] = True

        # result variable to count the number of connected components
        res = 0

        # iterate through all cities
        for i in range(N):
            if not visited[i]:
                res += 1
                helper(i)
        
        # return the total number of connected components
        return res
