class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split the words into a list
        words = s.split(" ")
        # check edge cases
        if len(pattern) != len(words):
            return False
        # hashmaps to map each character to word
        chToWord,wordToCh = {}, {}
        # check both at the same time using zip
        for ch, word in zip(pattern, words):
            # check if the current ch/word is already mapped
            if ch in chToWord and chToWord[ch] != word:
                return False
            if word in wordToCh and wordToCh[word] != ch:
                return False
            # map
            chToWord[ch] = word
            wordToCh[word] = ch
        return True
        