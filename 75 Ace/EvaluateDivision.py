class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # initialize a defaultdict to represent the graph
        graph = defaultdict(dict)
        # number of equations
        N = len(equations)
        # populate the graph with equations and values
        for i in range(N):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]
        # dfs function to find the result of queries
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1
            # if y is directly reachable from x, return the corresponding value
            if y in graph[x]:
                return graph[x][y]
            # explore neighbors of x recursively
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp == -1:
                        continue
                    else:
                        # return the product of current edge value and the value from the recursive call
                        return temp * graph[x][i]
            return -1

        res = []
        # process each query and append the result to the result list
        for p, q in queries:
            res.append(dfs(p, q, set()))
        return res
