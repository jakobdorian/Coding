class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adjacency list to represent the directed graph
        adj = collections.defaultdict(list)
        # populate the adjacency list based on prerequisites
        for course, pre in prerequisites:
            adj[pre].append(course)
        # dfs function to check for cycles in the graph
        def dfs(node, visited, tracker):
            visited[node] = True
            tracker[node] = True
            for n in adj[node]:
                if n not in tracker and dfs(n, visited, tracker):
                    return True
                elif n in visited:
                    return True
            visited.pop(node)
            return False
        tracker = {}
        # iterate through all courses and check for cycles using DFS
        for n in range(numCourses):
            visited = {}
            if n not in tracker and dfs(n, visited, tracker):
                return False
        # if no cycles are found, return True (courses can be finished)
        return True
