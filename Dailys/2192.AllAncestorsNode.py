class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 1. graph - to store the original directed graph.
        # 2. rev_graph - to store the reverse of the original graph for easier ancestor lookup.
        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        res = []
        # populate both graphs using the edges list.
        for u, v in edges:
            graph[u].append(v)
            rev_graph[v].append(u)
        # perform BFS on the reversed graph starting from a given node.
        # this will help find all the ancestors of the node.
        def bfs(node):
            q = deque([node])
            ancestors = set()
            while q:
                curr = q.popleft()
                for parent in rev_graph[curr]:
                    if parent not in ancestors:
                        ancestors.add(parent)
                        q.append(parent)

            return sorted(ancestors)
        # generate the ancestors list for each node from 0 to n-1.
        for node in range(n):
            res.append(bfs(node))
        return res
