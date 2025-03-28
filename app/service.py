from app.trie import Trie

class PrefixService:
    def __init__(self, word_list):
        self.trie = Trie()
        self.word_set = set(word_list)
        
        for word in word_list:
            self.trie.insert(word)

    def get_prefixes(self, keywords):
        result = {}
        for word in keywords:
            if word in self.word_set:
                result[word] = self.trie.find_unique_prefix(word)
            else:
                result[word] = "not_applicable"
        return result
