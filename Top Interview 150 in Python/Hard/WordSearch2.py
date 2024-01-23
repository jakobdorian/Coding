class TrieNode:
    def __init__(self):
        # initialize a Trie node with a dictionary to store children nodes and a flag to mark the end of a word.
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        # traverse through each character in the word.
        for char in word:
            # if the character is not in the children of the current node, create a new node.
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # mark the end of the word by setting the 'is_end_of_word' flag to True.
        node.is_end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create an instance of the Trie data structure.
        trie = Trie()
        # Iinsert each word from the input list into the Trie.
        for word in words:
            trie.insert(word)
        rows, cols = len(board), len(board[0])
        result = set()
        def dfs(node, row, col, path):
            char = board[row][col]
            # check if the character is not in the children of the current Trie node.
            if char not in node.children:
                return
            node = node.children[char]
            # check if the Trie has reached the end of a word.
            if node.is_end_of_word:
                result.add(path)
            original_char = board[row][col]
            board[row][col] = "#"
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # explore neighboring positions in all four directions.
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] != "#":
                    dfs(node, new_row, new_col, path + board[new_row][new_col])
            board[row][col] = original_char
        # iterate through each cell in the board and start DFS from each cell.
        for i in range(rows):
            for j in range(cols):
                dfs(trie.root, i, j, board[i][j])
        # return the list of found words.
        return list(result)
