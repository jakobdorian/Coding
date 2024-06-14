class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        
        for w in words:
            # create a counter for the current word to store character frequencies
            curr = Counter(w)
            # update the count dictionary to keep the minimum frequency of each character
            for ch in count:
                count[ch] = min(count[ch], curr[ch])
        
        res = []

        for ch in count:
            # append the character to the result list as many times as its frequency
            for i in range(count[ch]):
                res.append(ch)
        
        # return the list of common characters
        return res
