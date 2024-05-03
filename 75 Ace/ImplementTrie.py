class Node:
    def __init__(self):
        # initialize a Trie node with a dictionary to store children nodes and a flag to mark the end of a word.
        self.children = {}
        self.endof = False

class Trie:
    def __init__(self):
        # initialize a Trie with a root node.
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        # traverse through each letter in the word.
        for letter in word:
            # if the letter is not in the children of the current node, create a new node.
            if letter not in ptr.children:
                ptr.children[letter] = Node()
            ptr = ptr.children[letter]
        # mark the end of the word by setting the 'endof' flag to True.
        ptr.endof = True

    def search(self, word: str) -> bool:
        ptr = self.root
        # traverse through each letter in the word.
        for letter in word:
            # if the letter is not in the children of the current node, the word is not present.
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        # check if the endof flag is True, indicating that the word is present in the Trie.
        return ptr.endof

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        # traverse through each letter in the prefix.
        for letter in prefix:
            # if the letter is not in the children of the current node, there is no word with the given prefix.
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        # there is at least one word with the given prefix.
        return True

        