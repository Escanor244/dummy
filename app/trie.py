class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0  # Tracks how many words share this prefix

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Increase count for shared prefixes
        node.is_end_of_word = True

    def find_unique_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            prefix += char
            node = node.children.get(char)
            if node and node.count == 1:  # Found the unique prefix
                return prefix
        return word  # Default to full word if no unique prefix
