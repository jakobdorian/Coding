class UnionFind:
    def __init__(self, n):
        # initialize the parent and rank arrays.
        # parent array represents the parent of each node
        # rank array represents the rank (or depth) of each tree
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        # find the root of the node u.
        # perform path compression by making the found root the parent of u directly.
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # find the roots of the nodes u and v.
        root_u = self.find(u)
        root_v = self.find(v)

        # union by rank.
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                # make root_u the parent of root_v if its rank is higher.
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                # make root_v the parent of root_u if its rank is higher.
                self.parent[root_u] = root_v
            else:
                # if ranks are the same, make root_u the parent of root_v and increase the rank of root_u.
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # initialize two UnionFind instances for Alice and Bob.
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)

        # sort edges by type in descending order.
        # this ensures type 3 edges (usable by both Alice and Bob) are processed first.
        edges.sort(reverse=True, key=lambda x: x[0])

        # initialize counters for removed edges and edges used by Alice and Bob.
        removed_edges = 0
        alice_edges = 0
        bob_edges = 0

        # iterate over all edges.
        for edge_type, u, v in edges:
            u -= 1  # decrement node indices to convert to 0-based indexing.
            v -= 1

            if edge_type == 3:
                # if the edge is type 3, try to union in both Alice's and Bob's UnionFind instances.
                if uf_alice.union(u, v):
                    uf_bob.union(u, v)
                    alice_edges += 1
                    bob_edges += 1
                else:
                    # if the union operation fails, it means the edge is redundant.
                    removed_edges += 1
            elif edge_type == 1:
                # if the edge is type 1, try to union in Alice's UnionFind instance.
                if uf_alice.union(u, v):
                    alice_edges += 1
                else:
                    removed_edges += 1
            elif edge_type == 2:
                # if the edge is type 2, try to union in Bob's UnionFind instance.
                if uf_bob.union(u, v):
                    bob_edges += 1
                else:
                    removed_edges += 1

        # check if both Alice and Bob have fully connected graphs.
        if alice_edges == n - 1 and bob_edges == n - 1:
            return removed_edges
        else:
            return -1  # if either Alice or Bob's graph is not fully connected, return -1.
