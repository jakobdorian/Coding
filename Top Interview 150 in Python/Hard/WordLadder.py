class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # base case: check if the endWord is not in the wordList
        if endWord not in wordList:
            return 0
        neigh = collections.defaultdict(list)
        wordList.append(beginWord)
        # set to track visited words
        visited = set([beginWord])
        # deque for breadth-first search
        q = deque([beginWord])
        res = 1
        # populate the neighbors dictionary with word patterns
        for word in wordList:
            for pos in range(len(word)):
                pattern = word[:pos] + "*" + word[pos + 1:]
                neigh[pattern].append(word)
        # bfs
        while q:
            # process all words at the current level
            for i in range(len(q)):
                word = q.popleft()
                # check if the current word is the endWord
                if word == endWord:
                    return res
                # generate patterns for the current word and explore neighbors
                for pos in range(len(word)):
                    pattern = word[:pos] + "*" + word[pos + 1:]
                    for n in neigh[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            # increment ladder length after processing the current level
            res += 1
        # if the endWord is not reached, return 0
        return 0
