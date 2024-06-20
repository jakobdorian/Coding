from collections import deque

def bfs(n, m, edges, s):
    # visited array to keep track of visited nodes
    visited = [False] * (n+1)
    
    # initialize distances array to store shortest distances from node s
    distances = [-1] * (n+1)
    
    # create adjacency list for graph representation
    adj_list = [[] for i in range(n+1)]
    
    # build adjacency list from edges
    for x, y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    # initialize queue for BFS starting from node s with distance 0
    q = deque([(s, 0)])
    distances[s] = 0
    visited[s] = True
    
    # perform BFS
    while q:
        u, w = q.popleft()  # dequeue node u with distance w
        
        # explore neighbors of u
        for v in adj_list[u]:
            if not visited[v]:  # if v is not visited
                distances[v] = w + 6  # update distance of v from s
                q.append((v, w + 6))  # enqueue v with updated distance
                visited[v] = True  # mark v as visited
    
    distances.remove(0)  # remove distance from s to s (not needed)
    
    return distances[1:]  # return distances from node 1 to node n
