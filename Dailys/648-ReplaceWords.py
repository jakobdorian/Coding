class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # convert the list of dictionary words to a set for faster lookup
        dictionary = set(dictionary)
        res = []

        # split the sentence into individual words and iterate over each word
        for word in sentence.split(' '):
            found = False  # flag to check if a prefix is found in the dictionary
            # check each prefix of the word to see if it's in the dictionary
            for x in range(1, len(word)):
                if word[0:x] in dictionary:
                    found = True 
                    res.append(word[0:x])  # append the prefix to the result list
                    break
            if not found:
                # if no prefix is found, append the original word to the result list
                res.append(word)

        # join the result list into a single string with spaces and return it
        return " ".join(res)
