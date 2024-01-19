class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # initialize a queue with the starting gene and 0 steps
        q = deque([(startGene, 0)])
        choices = set(("A", "C", "G", "T"))
        # convert the bank list to a set for faster membership checks
        bank = set(bank)
        # keep track of visited genes to avoid revisiting them
        visited = {startGene}
        # bfs loop
        while q:
            # dequeue the current gene and its steps
            gene, steps = q.popleft()
            # check if the current gene is the target gene
            if gene == endGene:
                return steps
            # iterate through each character in the gene
            for i, s in enumerate(gene):
                # try each possible mutation at the current position
                for c in choices:
                    if s != c:
                        # create a new gene with the mutation
                        newGene = gene[:i] + c + gene[i+1:]
                        # check if the new gene is in the bank and not visited
                        if newGene not in visited and newGene in bank:
                            # mark the new gene as visited and enqueue it
                            visited.add(newGene)
                            q.append((newGene, steps + 1))
        # if the target gene is not reached, return -1
        return -1
        