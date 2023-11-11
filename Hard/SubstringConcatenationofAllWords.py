class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # edge cases
        # if len(s) == 0 or s is None or words in None:
        #     return []
        res = []
        # dict to keep word and count
        count = {}
        wordLength = len(words[0])
        wordsLength = len(words) * wordLength

        # fill count dict
        for word in words:
            count[word] = count.get(word, 0) + 1

        # find substrings using sliding window starting from LHS
        for l in range(len(s) - wordsLength + 1):
            # dict for words found
            found = {}
            # iterate through RHS of window to find words
            for r in range(len(words)):
                # where our word will start
                curr = l + r * wordLength
                temp = s[curr : curr + wordLength]
                if temp not in count:
                    break

                found[temp] = found.get(temp, 0) + 1
                # is the same word found twice?
                if found[temp] > count[temp]: 
                    break
            # make sure these two are the same
            if found == count:
                res.append(l)
        return res
        