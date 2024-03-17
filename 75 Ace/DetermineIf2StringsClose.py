class Solution:  
    def closeStrings(self, word1: str, word2: str) -> bool:
        # count occurrences of each character in both words
        c1, c2 = Counter(word1), Counter(word2)

        # count the occurrences of unique counts of characters in both words
        n1 = Counter([val for val in c1.values()])
        n2 = Counter([val for val in c2.values()])

        # check if two words are close:
        # either they have the same character counts or
        # they have the same set of characters and the same set of character counts
        return c1 == c2 or (n1 == n2 and set(word1) == set(word2))
        