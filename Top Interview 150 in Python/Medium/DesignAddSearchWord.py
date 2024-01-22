class WordDictionary:
    def __init__(self):
        # initialize the trie with an empty root node represented as a dictionary
        self.root = {}

    def addWord(self, word: str) -> None:
        # function to add a word to the trie
        curr = self.root
        # check if the word is not already present in the trie
        if not self.search(word):
            # traverse the trie and add each character of the word
            for i in range(len(word)):
                if word[i] not in curr:
                    curr[word[i]] = {}
                curr = curr[word[i]]
            # mark the end of the word with a special character "!"
            curr["!"] = {}

    def search(self, word: str) -> bool:
        curr = self.root
        # helper function to recursively search for the word in the trie
        def helper(start, curr):
            if start >= len(word):
                # if the end of the word is reached, check if it is marked with "!"
                return "!" in curr
            if word[start] == ".":
                # if the current character is ".", recursively search all possible paths
                for k, v in curr.items():
                    if helper(start + 1, v):
                        return True
                return False
            elif word[start] in curr:
                # if the current character is a letter, continue searching in the trie
                return helper(start + 1, curr[word[start]])
            else:
                # if the current character is not present in the trie, return False
                return False
        # start the search from the root of the trie
        return helper(0, curr)
