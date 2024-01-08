class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list to represent the directed graph
        adj = [[] for _ in range(numCourses)]
        # populate the adjacency list based on prerequisites
        for course, pre in prerequisites:
            adj[pre].append(course)
        stack = []          # stack to store the topological order
        visited = set()     # set to keep track of visited nodes during DFS
        tracker = set()     # set to detect cycles during DFS
        self.cycle = False   # flag to check if a cycle is detected

        # DFS function to explore the graph
        def dfs(node, visited, tracker, stack):
            visited.add(node)
            tracker.add(node)
            for nxt in adj[node]:
                # if the next node is already in the tracker, a cycle is detected
                if nxt in tracker:
                    self.cycle = True
                    break
                # if the next node is not visited, recursively call DFS
                if nxt not in visited:
                    dfs(nxt, visited, tracker, stack)
            tracker.remove(node)
            stack.append(node)
        # iterate through each node in the graph and perform DFS if not visited
        for node in range(numCourses):
            if node not in visited:
                dfs(node, visited, tracker, stack)
        # if a cycle is detected, return an empty list
        if self.cycle:
            return []
        # return the topological order (reverse the stack)
        return stack[::-1]
