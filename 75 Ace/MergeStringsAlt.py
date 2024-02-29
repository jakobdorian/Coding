class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # pointers for both words
        i, j = 0, 0
        # empty list to store the merged result
        res = []
        # iterate until either of the words ends
        while i < len(word1) and j < len(word2):
            # append characters alternatively from both words to the result list
            res.append(word1[i])
            res.append(word2[j])
            # move pointers to the next character in each word
            i += 1
            j += 1
        # append the remaining characters of both words, if any, to the result list
        res.append(word1[i:])
        res.append(word2[j:])
        # concatenate all characters in the result list and return the merged string
        return "".join(res)
