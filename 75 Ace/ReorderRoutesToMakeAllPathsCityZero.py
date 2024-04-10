class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # create an adjacency list to represent the graph
        adj_list = defaultdict(list)

        # populate the adjacency list with given connections
        for u, v in connections:
            # for each connection, add the connection from u to v with cost 1,
            # and the reverse connection from v to u with cost 0
            adj_list[u].append((v, 1))
            adj_list[v].append((u, 0))

        q = deque()
        visited = [False] * n
        # mark the starting node as visited
        visited[0] = True
        cost = 0
        # add the starting node to the queue
        q.append(0)

        # perform BFS traversal
        while len(q) > 0:
            # dequeue the current node
            curr = q.popleft()
            # iterate over its neighbors
            for v, c in adj_list[curr]:
                # if the neighbor has not been visited yet
                if not visited[v]:
                    # mark it as visited
                    visited[v] = True
                    # add the cost of the connection to the total cost
                    cost += c
                    # enqueue the neighbor
                    q.append(v)
        
        # return the total cost
        return cost
