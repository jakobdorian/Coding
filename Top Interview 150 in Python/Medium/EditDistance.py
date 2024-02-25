class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # cache to store the minimum edit distances
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # initialize the bottom-right corner of the cache with the lengths of remaining characters
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # fill the cache starting from the second-last row and column
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # if the characters match, no additional edit required, get the value from diagonal cell
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    # if characters don't match, choose the minimum among insertion, deletion, and substitution
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
        # return the minimum edit distance found at the top-left corner of the cache
        return cache[0][0]
